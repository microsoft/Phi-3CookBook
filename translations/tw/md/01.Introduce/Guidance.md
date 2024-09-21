### Guidance-AI 和 Phi 模型即服務 (MaaS)
我們將 [Guidance](https://github.com/guidance-ai/guidance) 引入到 Azure AI Studio 的 Phi-3.5-mini 無伺服器端點，通過定義適合應用程序的結構來使輸出更加可預測。使用 Guidance，你可以消除昂貴的重試次數，例如，可以限制模型從預定義的列表中選擇（例如醫療代碼），限制輸出為提供的上下文中的直接引用，或者遵循任何正則表達式。Guidance 在推理堆棧中逐個 token 引導模型，降低成本和延遲 30-50%，這使其成為 [Phi-3-mini 無伺服器端點](https://aka.ms/try-phi3.5mini) 的一個獨特且有價值的附加功能。

## [**Guidance-AI**](https://github.com/guidance-ai/guidance) 是一個旨在幫助開發人員高效創建和部署 AI 模型的框架。它專注於提供構建健壯 AI 應用程序的工具和最佳實踐。

當與 **Phi 模型即服務 (MaaS)** 結合使用時，它提供了一個強大的解決方案，用於部署既具成本效益又高性能的小型語言模型 (SLMs)。

**Guidance-AI** 是一個編程框架，旨在幫助開發人員更有效地控制和引導大型語言模型 (LLMs)。它允許對輸出進行精確結構化，與傳統的提示或微調方法相比，降低延遲和成本。

### Guidance-AI 的主要功能：
- **高效控制**：使開發人員能夠控制語言模型生成文本的方式，確保高質量和相關的輸出。
- **成本和延遲減少**：優化生成過程，使其更具成本效益和更快速。
- **靈活整合**：可與各種後端一起使用，包括 Transformers, llama.cpp, AzureAI, VertexAI 和 OpenAI。
- **豐富的輸出結構**：支持複雜的輸出結構，如條件語句、循環和工具使用，使生成清晰且可解析的結果變得更容易。
- **兼容性**：允許單個 Guidance 程序在多個後端上執行，增強了靈活性和易用性。

### 示例用例：
- **限制生成**：使用正則表達式和上下文無關文法來引導模型的輸出。
- **工具整合**：自動交錯控制和生成，例如在文本生成任務中使用計算器。

有關更多詳細信息和示例，你可以查看 [Guidance-AI GitHub repository](https://github.com/guidance-ai/guidance)。

[查看 Phi-3.5 示例](../../../../code/01.Introduce/guidance.ipynb)

### Phi 模型的主要特點：
1. **成本效益**：設計為在保持高性能的同時具有經濟性。
2. **低延遲**：適用於需要快速響應的實時應用程序。
3. **靈活性**：可部署在各種環境中，包括雲端、邊緣和離線場景。
4. **定制化**：模型可以使用特定領域的數據進行微調，以提高性能。
5. **安全和合規**：依據 Microsoft 的 AI 原則構建，確保問責制、透明性、公平性、可靠性、安全性、隱私和包容性。

### Phi 模型即服務 (MaaS):
Phi 模型通過推理 API 提供按需付費的計費系統，使其易於集成到你的應用程序中，無需大量前期成本。

### 開始使用 Phi-3:
要開始使用 Phi 模型，你可以探索 [Azure AI 模型目錄](https://ai.azure.com/explore/models) 或 [GitHub Marketplace Models](https://github.com/marketplace/models)，這裡提供了預構建和可定制的模型。此外，你還可以使用 [Azure AI Studio](https://ai.azure.com) 來開發和部署你的 AI 應用程序。

### 資源
[入門 Guidance 的示例 Notebook](../../../../code/01.Introduce/guidance.ipynb)

免責聲明：此翻譯由人工智能模型從原文翻譯而來，可能不完美。請審查輸出並進行任何必要的更正。