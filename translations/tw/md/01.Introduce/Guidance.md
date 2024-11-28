### Guidance-AI 和 Phi 模型即服务 (MaaS)
我們將 [Guidance](https://github.com/guidance-ai/guidance) 引入到 Azure AI Foundry 的 Phi-3.5-mini 無伺服器端點，透過定義適合應用程式的結構來使輸出更可預測。使用 Guidance，你可以消除昂貴的重試，並且可以，例如，限制模型從預定義的列表（例如醫療代碼）中選擇，限制輸出為提供的上下文中的直接引用，或遵循任何正則表達式。Guidance 在推理堆疊中逐個標記引導模型，將成本和延遲降低 30-50%，這使其成為 [Phi-3-mini 無伺服器端點](https://aka.ms/try-phi3.5mini) 的獨特且有價值的附加功能。

## [**Guidance-AI**](https://github.com/guidance-ai/guidance) 是一個幫助開發者高效創建和部署 AI 模型的框架。它專注於提供構建強大 AI 應用程式的工具和最佳實踐。

當與 **Phi 模型即服務 (MaaS)** 結合使用時，它提供了一個強大的解決方案，用於部署既具成本效益又高性能的小型語言模型 (SLMs)。

**Guidance-AI** 是一個編程框架，旨在幫助開發者更有效地控制和引導大型語言模型 (LLMs)。它允許精確地結構化輸出，與傳統的提示或微調方法相比，減少了延遲和成本。

### Guidance-AI 的主要特點：
- **高效控制**：使開發者能夠控制語言模型生成文本的方式，確保高質量和相關的輸出。
- **成本和延遲減少**：優化生成過程，使其更具成本效益且更快速。
- **靈活整合**：可與多種後端協同工作，包括 Transformers, llama.cpp, AzureAI, VertexAI 和 OpenAI。
- **豐富的輸出結構**：支持複雜的輸出結構，如條件語句、循環和工具使用，使生成的結果更清晰且易於解析。
- **兼容性**：允許單個 Guidance 程序在多個後端上執行，提高了靈活性和易用性。

### 範例用例：
- **約束生成**：使用正則表達式和上下文無關文法來引導模型的輸出。
- **工具整合**：自動交替控制和生成，例如在文本生成任務中使用計算器。

欲了解更多詳細信息和範例，可以查看 [Guidance-AI GitHub repository](https://github.com/guidance-ai/guidance)。

[查看 Phi-3.5 範例](../../../../code/01.Introduce/guidance.ipynb)

### Phi 模型的主要特點：
1. **成本效益**：設計上既經濟實惠又保持高性能。
2. **低延遲**：適合需要快速響應的實時應用程式。
3. **靈活性**：可以在多種環境中部署，包括雲端、邊緣和離線場景。
4. **定制化**：可以使用特定領域的數據進行微調以提高性能。
5. **安全和合規**：基於微軟的 AI 原則構建，確保責任、透明、公平、可靠、安全、隱私和包容性。

### Phi 模型即服務 (MaaS):
Phi 模型通過推理 API 提供按需計費系統，使其易於集成到你的應用程式中，而無需大量前期成本。

### 開始使用 Phi-3:
要開始使用 Phi 模型，你可以探索 [Azure AI model catalog](https://ai.azure.com/explore/models) 或 [GitHub Marketplace Models](https://github.com/marketplace/models)，這些平台提供預構建和可定制的模型。此外，你還可以使用 [Azure AI Foundry](https://ai.azure.com) 開發和部署你的 AI 應用程式。

### 資源
[Getting Started with Guidance 的範例筆記本](../../../../code/01.Introduce/guidance.ipynb)

**免責聲明**:
本文檔是使用基於機器的AI翻譯服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原文檔視為權威來源。對於關鍵信息，建議進行專業人工翻譯。我們對使用此翻譯所引起的任何誤解或誤釋不承擔責任。