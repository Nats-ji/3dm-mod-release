# 3DM MOD Release Action

[![Actions Status](https://github.com/Nats-ji/3dm-release-action/workflows/Lint/badge.svg)](https://github.com/Nats-ji/3dm-release-action/actions) [![Actions Status](https://github.com/Nats-ji/3dm-release-action/workflows/Integration%20Test/badge.svg)](https://github.com/Nats-ji/3dm-release-action/actions)

## Description

[中文描述](https://github.com/Nats-ji/3dm-release-action/blob/master/README_zh.md)

A github action for updating mod information and mod files on [3DM mod site](https://mod.3dmgame.com/).

You can use this Github Action to automate your mod release workflow, if the source code of your mod is hosted on Github.

With this Github Action you can have your mod automatically updated on 3DM mod site, whenever you publish a release on Github.

Special thanks to 小莫 for providing the mod updating API.

### Example workflow

```yaml
name: Release
on:
  release:
      types: [published] #trigger on publish new release

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Load release version #obtain release version number from tag name
        id: get_version
        run: echo "::set-output name=RELEASE_VERSION::${GITHUB_REF#refs/*/}"

      - name: Release to 3DM
        uses: Nats-ji/3dm-release-action@v1.0.0
        with:
          appid: ${{ secrets.APPID }}
          appkey: ${{ secrets.APPKEY }}
          mod_id: 548964
          mod_title: My Mod
          mod_version: ${{ steps.get_version.outputs.RELEASE_VERSION }}
          mod_content: README.md
          mod_filepath: release/my_mod_1.2.2.zip
```

### Inputs

| Input                      | Description                                                       | Example                  |
|----------------------------|-------------------------------------------------------------------|--------------------------|
| `appid`                    | APP ID for the mod uploading API                                  | ${{ secrets.APPID }}     |
| `appkey`                   | APP key for the mod uploading API                                 | ${{ secrets.APPKEY }}    |
| `mod_id`                   | The id of the mod you wish to upload                              | 548964                   |
| `mod_title` (optional)     | The title of your mod                                             | My mod                   |
| `mod_tags` (optional)      | The tags for you mod                                              | cyberpunk, cheat, script |
| `mod_version` (optional)   | The version of your mod                                           | v1.2.5                   |
| `mod_desc` (optional)      | A short description of your mod                                   | This is my mod           |
| `mod_content` (optional)   | File path to the Markdown file for Mod descriptions               | README.md                |
| `mod_filepath` (optional)  | Path to your mod file (file format: `zip/7z/rar`, max size: 10mb) | release/my_mod.zip       |

### Outputs

| Output      | Description               |
|-------------|---------------------------|
| `response`  | Response from the server  |

## Using outputs

```yaml
steps:
  - name: Release to 3DM
    id: 3dm_release
    uses: Nats-ji/3dm-release-action@v1.0.0
    with:
      appid: ${{ secrets.APPID }}
      appkey: ${{ secrets.APPKEY }}
      mod_id: 548964
      mod_title: My Mod
      mod_version: 1.2.2
      mod_filepath: release/my_mod_1.2.2.zip

- name: Check outputs
    run: |
    echo ${{ steps.3dm_release.outputs.RESPONSE }}
```
