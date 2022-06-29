# Doki Doki SB (Club)

## 心跳心跳煞笔（心停祖安煞笔部）

欢迎来到DDSB的开源项目，本工程使用Ren'Py制作，基于[DokiMod](https://revolution.dokimod.cn/)，使用前请详细阅读该项目的[GPL 3.0](https://github.com/sout233/DDSB/blob/main/LICENSE)协议。

本项目仅为DDLC的爱好者作品，与[Team Salvato](http://teamsalvato.com/)无关。

**警告：该储存库为alpha项目，随时有可能封存或删除。**

请遵守以上协议以后，开始编译与调试。

如遇到问题，请提交issues。


## 编译与调试

### 准备工作

1. 首先，下载并配置[Python](https://www.python.org/)环境。
    >建议版本：Python3.9.6，但理论上3.7以上版本都可以正常运行。

2. 然后[下载Ren'py SDK 7.4.5](https://www.renpy.org/release/7.4.5)并安装。
   >只能是7.4.5版本，其他版本会出现未知错误，DokiMod暂未向上兼容。

以下部分引用自 https://github.com/imgradeone/DDLCModTemplate-Chinese-next/blob/master/README.md ：使用 Ren'Py SDK 7 进行 Mod 开发

1. 前往 Releases 页面获取 [模板的最新版本](https://github.com/imgradeone/DDLCModTemplate-Chinese-next/releases)。（目前 Mod 模板暂无稳定版本，您可以使用 GitHub 的 `Use this template` 创建新工程）
   
2. 从 [DDLC.moe](https://ddlc.moe) 或者 [Steam](https://store.steampowered.com/app/698780/) 下载 DDLC 游戏，然后将 `DDLC-1.1.1-pc` 文件夹（对于 macOS 用户则为 `ddlc-mac`，对于 Steam 版本则为 `Doki Doki Literature Club`）复制到 Ren'Py SDK（`renpy-<version>-sdk`）文件夹（或者您在 Ren'Py SDK 中自定义的文件夹）。将文件夹重命名为你的 Mod 名称。
   
3. 将 Mod 模板 ZIP 包内的内容复制到您刚刚粘贴的 DDLC 文件夹内。如有提示，请允许替换所有文件。  
    > 对于 macOS，请右键单击 `ddlc-mac` 文件夹内的 DDLC.app，点击 `显示包内容`，然后将 `Contents/Resources/autorun` 文件夹内的文件复制过去。如有提示，请允许替换所有文件。  
    > 在 Ren'Py SDK 7 中，如果遇到意外启动失败，可能是因为 `game/scripts.rpa` 的冲突，您可以尝试删除该文件。

4. 下载 [中文字体包](https://revolution.dokimod.cn/modtemplate/chinesefonts/)，将下载的 ZIP 文件的内容解压并复制到 `<Mod 工程文件夹>/game/mod_assets/fonts` 文件夹。
   
5. 克隆DDSB储存库，解压到`game`文件夹中并**覆盖**。
   
6. 在 Ren'Py SDK 里启动项目。它应正常编译并启动游戏。
    > 有时候，启动项目可能不会发生任何事情，或者报错。您可以再次单击 `Launch Project` / `运行工程` ，此时工程应该可以正常启动。

7. **大功告成！**


<!--
3.在Ren'Py根目录中新建一个名为"DDSB"的文件夹，然后clone该项目并解压到DDSB文件夹中。

4.目前新版已无需额外下载补充包，若仓库过大下不动则可以尝试使用steam++加速

~~4.因为版权和GitHub限制问题，你需要额外下载补充包（链接见下方），并将其解压进`Ren'Py根目录\DDSB\game\`内~~

~~>[OneDrive](https://1drv.ms/u/s!AuVe_GpP6ZchlQ_oUvj8rt1okK7O?e=Gy6YeY)(建议）~~

~~>[百毒网盘](https://pan.baidu.com/s/1K12iMDH0Vy_yiluQAI53Fw)(取件码：5r4r)~~

5.启动renpy.exe，选中DDSB工程并单击**Launch Project**，你应该能看到工程正常的启动。

>你可以在Ren'py的**选项（preferences）**中将语言修改为**简体中文（Simplified Chinese）**

6.**大功告成！**
-->

## 日志

~~准备迫害纱世里~~

~~纱世理竟然是NTR？~~

## 注意事项

该工程里的字体并不符合规范，为了注重版权问题，我建议你浏览[DokiMod中文字体相关](https://dokimod.cn/moddev/font.html#%E5%8D%8E%E4%B8%BA-harmonyos-sans)。

如果你不知道该如何编写这个DDLC MOD，我建议你浏览[DokiMod开发文档](https://dokimod.cn/moddev/#%E5%BC%80%E5%8F%91-ddlc-mod-%E4%B8%8E%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%BC%80%E5%8F%91%E4%B8%80%E6%AC%BE-ren-py-%E8%A7%86%E8%A7%89%E5%B0%8F%E8%AF%B4%E7%9B%B8%E6%AF%94%E6%9C%89%E4%BB%80%E4%B9%88%E4%BC%98%E5%8A%BF)。

你可以随时提交Push，我以后会编写关于提交的相关内容。

你要你是DDLC爱好者，我们就是hxd（doge）

祝你好运！




