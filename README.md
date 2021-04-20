# 3DM MOD Release Action

[![Actions Status](https://github.com/Nats-ji/3dm-release-action/workflows/Lint/badge.svg)](https://github.com/Nats-ji/3dm-release-action/actions)
[![Actions Status](https://github.com/Nats-ji/3dm-release-action/workflows/Integration%20Test/badge.svg)](https://github.com/Nats-ji/3dm-release-action/actions)

## Description

A github action for updating mod information and mod files on [3DM mod site](https://mod.3dmgame.com/).

### Example workflow

```yaml
- name: Release to 3DM
  uses: Nats-ji/3dm-release-action@master
  with:
    appid: ${{ secrets.APPID }}
    appkey: ${{ secrets.APPKEY }}
    mod_id: 548964
    mod_title: My Mod
    mod_version: ${{ env.version }}
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `appid`  | APP ID for the mod uploading API |
| `appkey` | APP key for the mod uploading API |
| `mod_id` | The id of the mod you wish to upload |
| `mod_title` (optional) | The title of your mod |
| `mod_tags` (optional) | The tags for you mod |
| `mod_version` (optional) | The version of your mod |
| `mod_desc` (optional) | A short description of your mod |
| `mod_content` (optional) | A detailed description using Markdown |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `response`  | Response from the server  |

## Using outputs

```yaml
steps:
  - name: Release to 3DM
    id: 3dm_release
    uses: Nats-ji/3dm-release-action@master
    with:
      appid: ${{ secrets.APPID }}
      appkey: ${{ secrets.APPKEY }}
      mod_id: 548964
      mod_title: My Mod
      mod_version: ${{ env.version }}

- name: Check outputs
    run: |
    echo ${{ steps.3dm_release.outputs.RESPONSE }}
```
