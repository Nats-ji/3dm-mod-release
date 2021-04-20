# 3DM MOD Release Action

[![Actions Status](https://github.com/Nats-ji/3dm-release-action/workflows/Lint/badge.svg)](https://github.com/Nats-ji/3dm-release-action/actions) [![Actions Status](https://github.com/Nats-ji/3dm-release-action/workflows/Integration%20Test/badge.svg)](https://github.com/Nats-ji/3dm-release-action/actions)

## 简介

[English](https://github.com/Nats-ji/3dm-release-action/blob/master/README.md)

Github 地址: [https://github.com/Nats-ji/3dm-release-action](https://github.com/Nats-ji/3dm-release-action)

一个用来更新[3DM MOD站](https://mod.3dmgame.com/)里Mod信息和Mod文件的Github Action。

特别感谢小莫大佬提供Mod更新API。

### 示例 Workflow 文件

```yaml
name: Release
on:
  release:
      types: [published] #在发布Release时触发

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Load release version #获取Release的tag版本号
        id: get_version
        run: echo "::set-output name=RELEASE_VERSION::${GITHUB_REF#refs/*/}"

      - name: Release to 3DM
        uses: Nats-ji/3dm-release-action@master
        with:
          appid: ${{ secrets.APPID }} #调用储在github secrets里面的APPID
          appkey: ${{ secrets.APPKEY }} #调用储在github secrets里面的APPKEY
          mod_id: 548964
          mod_title: My Mod
          mod_version: ${{ steps.get_version.outputs.RELEASE_VERSION }} #调用上一步获取的版本号
          mod_content: README.md
```

### 输入参数

| 输入参数  | 描述 | 示例 |
| ---------|------|------|
| `appid` | Mod更新API的APPID | ${{ secrets.APPID }} |
| `appkey` | Mod更新API的APPKEY | ${{ secrets.APPKEY }} |
| `mod_id` | 你想要更新的Mod的ID号 | 548964 |
| `mod_title` （可选） | Mod的标题 | 我的Mod |
| `mod_tags` （可选） | Mod的标签 | 修改器, 中文, 原创 |
| `mod_version` （可选） | Mod的版本号 | v1.2.5 |
| `mod_desc` （可选） | Mod的简单描述 | 我的超强修改器Mod |
| `mod_content` （可选） | Mod的详情介绍的Markdown文件路径 | README.md |

### 输出

| 输出 | 描述 |
|------|-----|
| `response`  | 服务器的返回内容  |

## 如何使用输出

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
      mod_version: 1.2.2

- name: Check outputs
    run: |
    echo ${{ steps.3dm_release.outputs.RESPONSE }}
```
