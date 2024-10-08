# 贡献指南

本项目欢迎各种贡献和建议。大多数贡献需要您同意一个贡献者许可协议 (CLA)，声明您有权利并实际授予我们使用您贡献的权利。详情请访问 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

当您提交拉取请求时，CLA 机器人会自动确定您是否需要提供 CLA，并适当地装饰 PR（例如，状态检查、评论）。只需按照机器人提供的说明操作。您只需要在所有使用我们 CLA 的仓库中执行一次此操作。

## 行为准则

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/)。
更多信息请阅读 [行为准则 FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或联系 [opencode@microsoft.com](mailto:opencode@microsoft.com) 以获取任何其他问题或评论。

## 创建问题的注意事项

请不要为一般支持问题打开 GitHub 问题，因为 GitHub 列表应仅用于功能请求和错误报告。这样我们可以更轻松地跟踪代码中的实际问题或错误，并将一般讨论与实际代码分开。

## 如何贡献

### 拉取请求指南

在向 Phi-3 CookBook 仓库提交拉取请求 (PR) 时，请遵循以下指南：

- **Fork 仓库**：在进行修改之前，请始终将仓库 fork 到您自己的账户。

- **分开提交拉取请求 (PR)**：
  - 每种类型的更改应在单独的拉取请求中提交。例如，错误修复和文档更新应在不同的 PR 中提交。
  - 拼写错误修正和小的文档更新可以在适当情况下合并到一个 PR 中。

- **处理合并冲突**：如果您的拉取请求显示合并冲突，请在进行修改之前更新本地的 `main` 分支以镜像主仓库。

- **翻译提交**：提交翻译 PR 时，确保翻译文件夹包含原始文件夹中所有文件的翻译。

### 翻译指南

> [!IMPORTANT]
>
> 在翻译此仓库中的文本时，不要使用机器翻译。仅在您熟练的语言中志愿翻译。

如果您精通非英语语言，可以帮助翻译内容。请按照以下步骤确保您的翻译贡献得到正确整合：

- **创建翻译文件夹**：导航到相应的部分文件夹，并为您贡献的语言创建翻译文件夹。例如：
  - 对于介绍部分：`Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - 对于快速开始部分：`Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - 其他部分（03.Inference，04.Finetuning 等）继续此模式

- **更新相对路径**：翻译时，通过在相对路径的开头添加 `../../` 来调整文件夹结构，以确保链接正确。例如，将以下内容更改为：
  - 将 `(../../imgs/01/phi3aisafety.png)` 更改为 `(../../../../imgs/01/phi3aisafety.png)`

- **组织您的翻译**：每个翻译文件应放置在相应部分的翻译文件夹中。例如，如果您将介绍部分翻译成西班牙语，您将创建如下文件夹：
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **提交完整的 PR**：确保一个部分的所有翻译文件都包含在一个 PR 中。我们不接受部分翻译的提交。提交翻译 PR 时，请确保翻译文件夹包含原始文件夹中所有文件的翻译。

### 编写指南

为了确保所有文档的一致性，请使用以下指南：

- **URL 格式**：将所有 URL 用方括号括起来，后面跟上括号，中间没有任何额外的空格。例如：[example](https://example.com)。

- **相对链接**：使用 `./` 指向当前目录中的文件或文件夹，使用 `../` 指向父目录中的文件或文件夹。例如：[example](../../path/to/file) 或 [example](../../../path/to/file)。

- **非特定国家的语言环境**：确保您的链接不包含特定国家的语言环境。例如，避免使用 `/en-us/` 或 `/en/`。

- **图片存储**：将所有图片存储在 `./imgs` 文件夹中。

- **描述性图片名称**：使用英文字符、数字和短划线为图片命名。例如：`example-image.jpg`。

## GitHub 工作流程

当您提交拉取请求时，将触发以下工作流程来验证更改。请按照以下说明确保您的拉取请求通过工作流程检查：

- [检查断开的相对路径](../..)
- [检查 URL 中不包含语言环境](../..)

### 检查断开的相对路径

此工作流程确保您文件中的所有相对路径都是正确的。

1. 要确保您的链接正常工作，请使用 VS Code 执行以下任务：
    - 将鼠标悬停在文件中的任何链接上。
    - 按 **Ctrl + Click** 导航到链接。
    - 如果您点击链接并且它在本地不起作用，它将触发工作流程并且在 GitHub 上也不起作用。

1. 要解决此问题，请使用 VS Code 提供的路径建议执行以下任务：
    - 输入 `./` 或 `../`。
    - VS Code 将根据您输入的内容提示您选择可用选项。
    - 通过点击所需的文件或文件夹来确保路径正确。

添加正确的相对路径后，保存并推送您的更改。

### 检查 URL 中不包含语言环境

此工作流程确保任何网页 URL 不包含特定国家的语言环境。由于此仓库是全球可访问的，因此确保 URL 不包含您的国家语言环境非常重要。

1. 要验证您的 URL 中没有国家语言环境，请执行以下任务：

    - 检查 URL 中是否有 `/en-us/`、`/en/` 或任何其他语言环境的文本。
    - 如果这些文本不在您的 URL 中，那么您将通过此检查。

1. 要解决此问题，请执行以下任务：
    - 打开工作流程高亮显示的文件路径。
    - 从 URL 中删除国家语言环境。

删除国家语言环境后，保存并推送您的更改。

### 检查断开的 URL

此工作流程确保文件中的任何网页 URL 都能正常工作并返回 200 状态码。

1. 要验证您的 URL 是否正常工作，请执行以下任务：
    - 检查文件中 URL 的状态。

2. 要修复任何断开的 URL，请执行以下任务：
    - 打开包含断开 URL 的文件。
    - 将 URL 更新为正确的 URL。

修复 URL 后，保存并推送您的更改。

> [!NOTE]
>
> 可能存在 URL 检查失败的情况，即使链接是可访问的。这可能由于以下原因之一：
>
> - **网络限制**：GitHub actions 服务器可能有网络限制，无法访问某些 URL。
> - **超时问题**：响应时间过长的 URL 可能会在工作流程中触发超时错误。
> - **临时服务器问题**：偶尔的服务器停机或维护可能会在验证期间使 URL 暂时不可用。

