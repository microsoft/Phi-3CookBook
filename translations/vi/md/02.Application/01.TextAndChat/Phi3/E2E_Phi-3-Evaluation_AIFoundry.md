# Đánh giá Mô hình Phi-3 / Phi-3.5 Tùy chỉnh trong Azure AI Foundry Tập trung vào Nguyên tắc AI Có Trách nhiệm của Microsoft

Mẫu end-to-end (E2E) này dựa trên hướng dẫn "[Đánh giá Mô hình Phi-3 / 3.5 Tùy chỉnh trong Azure AI Foundry Tập trung vào AI Có Trách nhiệm của Microsoft](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" từ Microsoft Tech Community.

## Tổng quan

### Làm thế nào để đánh giá mức độ an toàn và hiệu suất của một mô hình Phi-3 / Phi-3.5 tùy chỉnh trong Azure AI Foundry?

Việc tùy chỉnh mô hình đôi khi có thể dẫn đến các phản hồi không mong muốn hoặc không phù hợp. Để đảm bảo mô hình an toàn và hiệu quả, điều quan trọng là đánh giá khả năng của mô hình trong việc tạo nội dung có hại cũng như khả năng tạo ra các phản hồi chính xác, phù hợp và mạch lạc. Trong hướng dẫn này, bạn sẽ học cách đánh giá mức độ an toàn và hiệu suất của mô hình Phi-3 / Phi-3.5 tùy chỉnh tích hợp với Prompt flow trong Azure AI Foundry.

Dưới đây là quy trình đánh giá của Azure AI Foundry.

![Kiến trúc của hướng dẫn.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.vi.png)

*Nguồn ảnh: [Đánh giá các ứng dụng AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Để biết thêm thông tin chi tiết và khám phá các tài nguyên bổ sung về Phi-3 / Phi-3.5, vui lòng truy cập [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Yêu cầu

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Mô hình Phi-3 / Phi-3.5 tùy chỉnh

### Mục lục

1. [**Kịch bản 1: Giới thiệu về đánh giá Prompt flow trong Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Giới thiệu về đánh giá an toàn](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Giới thiệu về đánh giá hiệu suất](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Kịch bản 2: Đánh giá mô hình Phi-3 / Phi-3.5 trong Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Trước khi bắt đầu](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Triển khai Azure OpenAI để đánh giá mô hình Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Đánh giá mô hình Phi-3 / Phi-3.5 tùy chỉnh bằng Prompt flow trong Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Chúc mừng!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Kịch bản 1: Giới thiệu về đánh giá Prompt flow trong Azure AI Foundry**

### Giới thiệu về đánh giá an toàn

Để đảm bảo rằng mô hình AI của bạn là đạo đức và an toàn, điều quan trọng là đánh giá nó dựa trên Nguyên tắc AI Có Trách nhiệm của Microsoft. Trong Azure AI Foundry, đánh giá an toàn cho phép bạn đánh giá tính dễ bị tấn công của mô hình trước các cuộc tấn công jailbreak và khả năng tạo nội dung có hại, phù hợp trực tiếp với các nguyên tắc này.

![Đánh giá an toàn.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.vi.png)

*Nguồn ảnh: [Đánh giá các ứng dụng AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Nguyên tắc AI Có Trách nhiệm của Microsoft

Trước khi bắt đầu các bước kỹ thuật, điều cần thiết là phải hiểu các Nguyên tắc AI Có Trách nhiệm của Microsoft, một khung đạo đức được thiết kế để hướng dẫn phát triển, triển khai và vận hành AI một cách có trách nhiệm. Các nguyên tắc này đảm bảo rằng các công nghệ AI được xây dựng theo cách công bằng, minh bạch và bao trùm. Đây là nền tảng để đánh giá mức độ an toàn của các mô hình AI.

Các Nguyên tắc AI Có Trách nhiệm của Microsoft bao gồm:

- **Công bằng và Bao trùm**: Các hệ thống AI nên đối xử công bằng với tất cả mọi người và tránh ảnh hưởng đến các nhóm người tương tự nhau theo cách khác nhau. Ví dụ, khi các hệ thống AI đưa ra hướng dẫn về điều trị y tế, đơn xin vay tiền hoặc việc làm, chúng nên đưa ra khuyến nghị giống nhau cho tất cả những người có các triệu chứng, hoàn cảnh tài chính hoặc trình độ chuyên môn tương tự.

- **Độ tin cậy và An toàn**: Để xây dựng niềm tin, điều quan trọng là các hệ thống AI hoạt động đáng tin cậy, an toàn và nhất quán. Các hệ thống này nên hoạt động như được thiết kế ban đầu, phản ứng an toàn với các điều kiện không lường trước và chống lại sự thao túng có hại. Cách chúng hoạt động và phạm vi các điều kiện mà chúng có thể xử lý phản ánh các tình huống và hoàn cảnh mà các nhà phát triển đã dự đoán trong quá trình thiết kế và thử nghiệm.

- **Minh bạch**: Khi các hệ thống AI giúp đưa ra các quyết định có tác động lớn đến cuộc sống của con người, điều quan trọng là mọi người phải hiểu cách các quyết định đó được đưa ra. Ví dụ, một ngân hàng có thể sử dụng hệ thống AI để quyết định liệu một người có đủ điều kiện vay tín dụng hay không. Một công ty có thể sử dụng hệ thống AI để xác định những ứng viên đủ điều kiện nhất để tuyển dụng.

- **Quyền riêng tư và Bảo mật**: Khi AI trở nên phổ biến hơn, việc bảo vệ quyền riêng tư và bảo mật thông tin cá nhân và doanh nghiệp ngày càng trở nên quan trọng và phức tạp. Với AI, quyền riêng tư và bảo mật dữ liệu cần được chú ý kỹ lưỡng vì việc truy cập dữ liệu là cần thiết để các hệ thống AI đưa ra dự đoán và quyết định chính xác và có cơ sở về con người.

- **Trách nhiệm giải trình**: Những người thiết kế và triển khai các hệ thống AI phải chịu trách nhiệm về cách các hệ thống của họ hoạt động. Các tổ chức nên dựa vào các tiêu chuẩn ngành để phát triển các chuẩn mực trách nhiệm giải trình. Các chuẩn mực này có thể đảm bảo rằng các hệ thống AI không phải là thẩm quyền cuối cùng đối với bất kỳ quyết định nào ảnh hưởng đến cuộc sống của con người. Chúng cũng có thể đảm bảo rằng con người duy trì quyền kiểm soát có ý nghĩa đối với các hệ thống AI tự động cao.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.vi.png)

*Nguồn ảnh: [AI Có Trách nhiệm là gì?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Để tìm hiểu thêm về Nguyên tắc AI Có Trách nhiệm của Microsoft, hãy truy cập [AI Có Trách nhiệm là gì?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Các chỉ số an toàn

Trong hướng dẫn này, bạn sẽ đánh giá mức độ an toàn của mô hình Phi-3 tùy chỉnh bằng các chỉ số an toàn của Azure AI Foundry. Các chỉ số này giúp bạn đánh giá khả năng của mô hình trong việc tạo nội dung có hại và tính dễ bị tấn công bởi các cuộc tấn công jailbreak. Các chỉ số an toàn bao gồm:

- **Nội dung liên quan đến tự làm hại bản thân**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung liên quan đến tự làm hại bản thân hay không.
- **Nội dung thù hận và không công bằng**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung thù hận hoặc không công bằng hay không.
- **Nội dung bạo lực**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung bạo lực hay không.
- **Nội dung tình dục**: Đánh giá liệu mô hình có xu hướng tạo ra nội dung tình dục không phù hợp hay không.

Việc đánh giá các khía cạnh này đảm bảo rằng mô hình AI không tạo ra nội dung có hại hoặc xúc phạm, phù hợp với các giá trị xã hội và tiêu chuẩn quy định.

![Đánh giá dựa trên an toàn.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.vi.png)

### Giới thiệu về đánh giá hiệu suất

Để đảm bảo rằng mô hình AI của bạn hoạt động như mong đợi, điều quan trọng là đánh giá hiệu suất của nó dựa trên các chỉ số hiệu suất. Trong Azure AI Foundry, đánh giá hiệu suất cho phép bạn đánh giá mức độ hiệu quả của mô hình trong việc tạo ra các phản hồi chính xác, phù hợp và mạch lạc.

![Đánh giá hiệu suất.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.vi.png)

*Nguồn ảnh: [Đánh giá các ứng dụng AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Các chỉ số hiệu suất

Trong hướng dẫn này, bạn sẽ đánh giá hiệu suất của mô hình Phi-3 / Phi-3.5 tùy chỉnh bằng các chỉ số hiệu suất của Azure AI Foundry. Các chỉ số này giúp bạn đánh giá mức độ hiệu quả của mô hình trong việc tạo ra các phản hồi chính xác, phù hợp và mạch lạc. Các chỉ số hiệu suất bao gồm:

- **Groundedness**: Đánh giá mức độ phù hợp của các câu trả lời được tạo ra với thông tin từ nguồn đầu vào.
- **Relevance**: Đánh giá mức độ liên quan của các phản hồi được tạo ra với các câu hỏi được đưa ra.
- **Coherence**: Đánh giá mức độ mạch lạc của văn bản được tạo ra, liệu nó có trôi chảy và giống như ngôn ngữ của con người hay không.
- **Fluency**: Đánh giá mức độ thông thạo ngôn ngữ của văn bản được tạo ra.
- **GPT Similarity**: So sánh phản hồi được tạo ra với sự thật gốc để đánh giá mức độ tương đồng.
- **F1 Score**: Tính tỷ lệ từ ngữ được chia sẻ giữa phản hồi được tạo ra và dữ liệu nguồn.

Các chỉ số này giúp bạn đánh giá mức độ hiệu quả của mô hình trong việc tạo ra các phản hồi chính xác, phù hợp và mạch lạc.

![Đánh giá dựa trên hiệu suất.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.vi.png)

## **Kịch bản 2: Đánh giá mô hình Phi-3 / Phi-3.5 trong Azure AI Foundry**

### Trước khi bắt đầu

Hướng dẫn này là phần tiếp theo của các bài viết trước, "[Tùy chỉnh và Tích hợp Mô hình Phi-3 với Prompt Flow: Hướng dẫn Từng Bước](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" và "[Tùy chỉnh và Tích hợp Mô hình Phi-3 với Prompt Flow trong Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Trong các bài viết này, chúng tôi đã hướng dẫn quy trình tùy chỉnh mô hình Phi-3 / Phi-3.5 trong Azure AI Foundry và tích hợp nó với Prompt flow.

Trong hướng dẫn này, bạn sẽ triển khai một mô hình Azure OpenAI làm công cụ đánh giá trong Azure AI Foundry và sử dụng nó để đánh giá mô hình Phi-3 / Phi-3.5 tùy chỉnh của mình.

Trước khi bắt đầu hướng dẫn này, hãy đảm bảo rằng bạn đã chuẩn bị các yêu cầu sau, như đã mô tả trong các bài viết trước:

1. Một tập dữ liệu đã chuẩn bị để đánh giá mô hình Phi-3 / Phi-3.5 tùy chỉnh.
1. Một mô hình Phi-3 / Phi-3.5 đã được tùy chỉnh và triển khai trong Azure Machine Learning.
1. Một Prompt flow được tích hợp với mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn trong Azure AI Foundry.

> [!NOTE]
> Bạn sẽ sử dụng tệp *test_data.jsonl*, nằm trong thư mục dữ liệu từ tập dữ liệu **ULTRACHAT_200k** đã được tải xuống trong các bài viết trước, làm tập dữ liệu để đánh giá mô hình Phi-3 / Phi-3.5 tùy chỉnh.

#### Tích hợp mô hình Phi-3 / Phi-3.5 tùy chỉnh với Prompt flow trong Azure AI Foundry (Phương pháp mã trước)

> [!NOTE]
> Nếu bạn đã thực hiện phương pháp không cần mã được mô tả trong "[Tùy chỉnh và Tích hợp Mô hình Phi-3 với Prompt Flow trong Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", bạn có thể bỏ qua bài tập này và chuyển sang bài tiếp theo.
> Tuy nhiên, nếu bạn đã thực hiện phương pháp mã trước được mô tả trong "[Tùy chỉnh và Tích hợp Mô hình Phi-3 với Prompt Flow: Hướng dẫn Từng Bước](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" để tùy chỉnh và triển khai mô hình Phi-3 / Phi-3.5 của mình, quy trình kết nối mô hình của bạn với Prompt flow sẽ hơi khác. Bạn sẽ học quy trình này trong bài tập này.

Để tiếp tục, bạn cần tích hợp mô hình Phi-3 / Phi-3.5 tùy chỉnh của mình vào Prompt flow trong Azure AI Foundry.

#### Tạo Hub Azure AI Foundry

Bạn cần tạo một Hub trước khi tạo Dự án. Một Hub hoạt động như một Nhóm Tài nguyên, cho phép bạn tổ chức và quản lý nhiều Dự án trong Azure AI Foundry.

1. Đăng nhập vào [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Chọn **All hubs** từ tab bên trái.

1. Chọn **+ New hub** từ menu điều hướng.

    ![Tạo hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.vi.png)

1. Thực hiện các tác vụ sau:

    - Nhập **Hub name**. Tên này phải là một giá trị duy nhất.
    - Chọn **Subscription** Azure của bạn.
    - Chọn **Resource group** để sử dụng (tạo mới nếu cần).
    - Chọn **Location** bạn muốn sử dụng.
    - Chọn **Connect Azure AI Services** để sử dụng (tạo mới nếu cần).
    - Chọn **Connect Azure AI Search** để **Bỏ qua kết nối**.
![Điền hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.vi.png)

1. Chọn **Next**.

#### Tạo Dự Án Azure AI Foundry

1. Trong Hub mà bạn đã tạo, chọn **All projects** từ thanh bên trái.

1. Chọn **+ New project** từ menu điều hướng.

    ![Chọn dự án mới.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.vi.png)

1. Nhập **Project name**. Tên dự án phải là một giá trị duy nhất.

    ![Tạo dự án.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.vi.png)

1. Chọn **Create a project**.

#### Thêm kết nối tùy chỉnh cho mô hình Phi-3 / Phi-3.5 đã tinh chỉnh

Để tích hợp mô hình Phi-3 / Phi-3.5 tùy chỉnh với Prompt flow, bạn cần lưu endpoint và key của mô hình trong một kết nối tùy chỉnh. Thiết lập này đảm bảo quyền truy cập vào mô hình Phi-3 / Phi-3.5 tùy chỉnh trong Prompt flow.

#### Thiết lập api key và endpoint uri của mô hình Phi-3 / Phi-3.5 đã tinh chỉnh

1. Truy cập [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Điều hướng đến không gian làm việc Azure Machine Learning mà bạn đã tạo.

1. Chọn **Endpoints** từ thanh bên trái.

    ![Chọn endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.vi.png)

1. Chọn endpoint mà bạn đã tạo.

    ![Chọn endpoints đã tạo.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.vi.png)

1. Chọn **Consume** từ menu điều hướng.

1. Sao chép **REST endpoint** và **Primary key** của bạn.

    ![Sao chép api key và endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.vi.png)

#### Thêm Kết Nối Tùy Chỉnh

1. Truy cập [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Điều hướng đến dự án Azure AI Foundry mà bạn đã tạo.

1. Trong Dự Án mà bạn đã tạo, chọn **Settings** từ thanh bên trái.

1. Chọn **+ New connection**.

    ![Chọn kết nối mới.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.vi.png)

1. Chọn **Custom keys** từ menu điều hướng.

    ![Chọn custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.vi.png)

1. Thực hiện các bước sau:

    - Chọn **+ Add key value pairs**.
    - Đối với tên key, nhập **endpoint** và dán endpoint mà bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Chọn **+ Add key value pairs** lần nữa.
    - Đối với tên key, nhập **key** và dán key mà bạn đã sao chép từ Azure ML Studio vào trường giá trị.
    - Sau khi thêm các key, chọn **is secret** để ngăn key bị lộ.

    ![Thêm kết nối.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.vi.png)

1. Chọn **Add connection**.

#### Tạo Prompt flow

Bạn đã thêm một kết nối tùy chỉnh trong Azure AI Foundry. Bây giờ, hãy tạo một Prompt flow bằng các bước sau. Sau đó, bạn sẽ kết nối Prompt flow này với kết nối tùy chỉnh để sử dụng mô hình đã tinh chỉnh trong Prompt flow.

1. Điều hướng đến dự án Azure AI Foundry mà bạn đã tạo.

1. Chọn **Prompt flow** từ thanh bên trái.

1. Chọn **+ Create** từ menu điều hướng.

    ![Chọn Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.vi.png)

1. Chọn **Chat flow** từ menu điều hướng.

    ![Chọn chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.vi.png)

1. Nhập **Folder name** để sử dụng.

    ![Chọn chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.vi.png)

1. Chọn **Create**.

#### Thiết lập Prompt flow để trò chuyện với mô hình Phi-3 / Phi-3.5 tùy chỉnh

Bạn cần tích hợp mô hình Phi-3 / Phi-3.5 đã tinh chỉnh vào một Prompt flow. Tuy nhiên, Prompt flow hiện tại không được thiết kế cho mục đích này. Vì vậy, bạn cần thiết kế lại Prompt flow để tích hợp mô hình tùy chỉnh.

1. Trong Prompt flow, thực hiện các bước sau để xây dựng lại flow hiện tại:

    - Chọn **Raw file mode**.
    - Xóa tất cả mã hiện tại trong tệp *flow.dag.yml*.
    - Thêm mã sau vào tệp *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Chọn **Save**.

    ![Chọn raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.vi.png)

1. Thêm mã sau vào *integrate_with_promptflow.py* để sử dụng mô hình Phi-3 / Phi-3.5 tùy chỉnh trong Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Dán mã prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.vi.png)

> [!NOTE]
> Để biết thêm thông tin chi tiết về cách sử dụng Prompt flow trong Azure AI Foundry, bạn có thể tham khảo [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chọn **Chat input**, **Chat output** để bật trò chuyện với mô hình của bạn.

    ![Chọn Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.vi.png)

1. Bây giờ bạn đã sẵn sàng để trò chuyện với mô hình Phi-3 / Phi-3.5 tùy chỉnh của mình. Trong bài thực hành tiếp theo, bạn sẽ học cách khởi động Prompt flow và sử dụng nó để trò chuyện với mô hình Phi-3 / Phi-3.5 đã tinh chỉnh.

> [!NOTE]
>
> Prompt flow đã được xây dựng lại sẽ trông giống như hình dưới đây:
>
> ![Ví dụ Flow](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.vi.png)
>

#### Khởi động Prompt flow

1. Chọn **Start compute sessions** để khởi động Prompt flow.

    ![Khởi động compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.vi.png)

1. Chọn **Validate and parse input** để làm mới các tham số.

    ![Xác thực input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.vi.png)

1. Chọn **Value** của **connection** tới kết nối tùy chỉnh bạn đã tạo. Ví dụ: *connection*.

    ![Kết nối.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.vi.png)

#### Trò chuyện với mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn

1. Chọn **Chat**.

    ![Chọn chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.vi.png)

1. Đây là một ví dụ về kết quả: Bây giờ bạn có thể trò chuyện với mô hình Phi-3 / Phi-3.5 tùy chỉnh của mình. Nên đặt câu hỏi dựa trên dữ liệu đã sử dụng để tinh chỉnh.

    ![Trò chuyện với prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.vi.png)

### Triển khai Azure OpenAI để đánh giá mô hình Phi-3 / Phi-3.5

Để đánh giá mô hình Phi-3 / Phi-3.5 trong Azure AI Foundry, bạn cần triển khai một mô hình Azure OpenAI. Mô hình này sẽ được sử dụng để đánh giá hiệu suất của mô hình Phi-3 / Phi-3.5.

#### Triển khai Azure OpenAI

1. Đăng nhập vào [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Điều hướng đến dự án Azure AI Foundry mà bạn đã tạo.

    ![Chọn Dự Án.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.vi.png)

1. Trong Dự Án mà bạn đã tạo, chọn **Deployments** từ thanh bên trái.

1. Chọn **+ Deploy model** từ menu điều hướng.

1. Chọn **Deploy base model**.

    ![Chọn Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.vi.png)

1. Chọn mô hình Azure OpenAI mà bạn muốn sử dụng. Ví dụ: **gpt-4o**.

    ![Chọn mô hình Azure OpenAI bạn muốn sử dụng.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.vi.png)

1. Chọn **Confirm**.

### Đánh giá mô hình Phi-3 / Phi-3.5 đã tinh chỉnh bằng Prompt flow của Azure AI Foundry

### Bắt đầu một đánh giá mới

1. Truy cập [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Điều hướng đến dự án Azure AI Foundry mà bạn đã tạo.

    ![Chọn Dự Án.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.vi.png)

1. Trong Dự Án mà bạn đã tạo, chọn **Evaluation** từ thanh bên trái.

1. Chọn **+ New evaluation** từ menu điều hướng.
![Chọn đánh giá.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.vi.png)

1. Chọn **Prompt flow** evaluation.

    ![Chọn Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.vi.png)

1. Thực hiện các bước sau:

    - Nhập tên đánh giá. Tên này phải là duy nhất.
    - Chọn **Question and answer without context** làm loại nhiệm vụ. Bởi vì, tập dữ liệu **UlTRACHAT_200k** được sử dụng trong hướng dẫn này không chứa ngữ cảnh.
    - Chọn prompt flow bạn muốn đánh giá.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.vi.png)

1. Chọn **Next**.

1. Thực hiện các bước sau:

    - Chọn **Add your dataset** để tải lên tập dữ liệu. Ví dụ, bạn có thể tải lên tệp tập dữ liệu kiểm tra, chẳng hạn như *test_data.json1*, được bao gồm khi bạn tải xuống tập dữ liệu **ULTRACHAT_200k**.
    - Chọn **Dataset column** phù hợp với tập dữ liệu của bạn. Ví dụ, nếu bạn đang sử dụng tập dữ liệu **ULTRACHAT_200k**, chọn **${data.prompt}** làm cột tập dữ liệu.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.vi.png)

1. Chọn **Next**.

1. Thực hiện các bước sau để cấu hình các chỉ số hiệu suất và chất lượng:

    - Chọn các chỉ số hiệu suất và chất lượng bạn muốn sử dụng.
    - Chọn mô hình Azure OpenAI mà bạn đã tạo để đánh giá. Ví dụ, chọn **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.vi.png)

1. Thực hiện các bước sau để cấu hình các chỉ số rủi ro và an toàn:

    - Chọn các chỉ số rủi ro và an toàn bạn muốn sử dụng.
    - Chọn ngưỡng để tính tỷ lệ lỗi mà bạn muốn sử dụng. Ví dụ, chọn **Medium**.
    - Đối với **question**, chọn **Data source** là **{$data.prompt}**.
    - Đối với **answer**, chọn **Data source** là **{$run.outputs.answer}**.
    - Đối với **ground_truth**, chọn **Data source** là **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.vi.png)

1. Chọn **Next**.

1. Chọn **Submit** để bắt đầu đánh giá.

1. Quá trình đánh giá sẽ mất một khoảng thời gian để hoàn thành. Bạn có thể theo dõi tiến trình trong tab **Evaluation**.

### Xem lại kết quả đánh giá

> [!NOTE]
> Các kết quả được trình bày dưới đây nhằm minh họa quá trình đánh giá. Trong hướng dẫn này, chúng tôi đã sử dụng một mô hình được tinh chỉnh trên tập dữ liệu tương đối nhỏ, điều này có thể dẫn đến kết quả không tối ưu. Kết quả thực tế có thể thay đổi đáng kể tùy thuộc vào kích thước, chất lượng, và sự đa dạng của tập dữ liệu được sử dụng, cũng như cấu hình cụ thể của mô hình.

Khi quá trình đánh giá hoàn tất, bạn có thể xem lại kết quả cho cả các chỉ số hiệu suất và an toàn.

1. Chỉ số hiệu suất và chất lượng:

    - Đánh giá hiệu quả của mô hình trong việc tạo ra các phản hồi mạch lạc, lưu loát và phù hợp.

    ![Kết quả đánh giá.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.vi.png)

1. Chỉ số rủi ro và an toàn:

    - Đảm bảo rằng các đầu ra của mô hình an toàn và tuân thủ các Nguyên tắc AI có trách nhiệm, tránh nội dung có hại hoặc xúc phạm.

    ![Kết quả đánh giá.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.vi.png)

1. Bạn có thể cuộn xuống để xem **Kết quả chỉ số chi tiết**.

    ![Kết quả đánh giá.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.vi.png)

1. Bằng cách đánh giá mô hình Phi-3 / Phi-3.5 tùy chỉnh của bạn dựa trên cả chỉ số hiệu suất và an toàn, bạn có thể xác nhận rằng mô hình không chỉ hiệu quả mà còn tuân thủ các thực hành AI có trách nhiệm, sẵn sàng để triển khai trong thực tế.

## Chúc mừng!

### Bạn đã hoàn thành hướng dẫn này

Bạn đã đánh giá thành công mô hình Phi-3 được tinh chỉnh tích hợp với Prompt flow trong Azure AI Foundry. Đây là một bước quan trọng để đảm bảo rằng các mô hình AI của bạn không chỉ hoạt động tốt mà còn tuân thủ các nguyên tắc AI có trách nhiệm của Microsoft, giúp bạn xây dựng các ứng dụng AI đáng tin cậy và an toàn.

![Kiến trúc.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.vi.png)

## Dọn dẹp tài nguyên Azure

Dọn dẹp các tài nguyên Azure của bạn để tránh các khoản phí bổ sung vào tài khoản. Truy cập cổng thông tin Azure và xóa các tài nguyên sau:

- Tài nguyên Azure Machine learning.
- Điểm cuối mô hình Azure Machine learning.
- Tài nguyên Dự án Azure AI Foundry.
- Tài nguyên Prompt flow của Azure AI Foundry.

### Các bước tiếp theo

#### Tài liệu

- [Đánh giá hệ thống AI bằng bảng điều khiển AI có trách nhiệm](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Chỉ số đánh giá và giám sát cho AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Tài liệu Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Tài liệu Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Nội dung đào tạo

- [Giới thiệu về Cách tiếp cận AI có trách nhiệm của Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Giới thiệu về Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Tham khảo

- [AI có trách nhiệm là gì?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Công bố các công cụ mới trong Azure AI giúp bạn xây dựng các ứng dụng AI tạo sinh an toàn và đáng tin cậy hơn](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Đánh giá các ứng dụng AI tạo sinh](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.