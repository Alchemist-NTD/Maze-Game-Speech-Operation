# Speech Recognition Application in Maze Game

## 1. Mô tả chung
Dự án này có mục đích ứng dụng các lý thuyết, phương pháp trong Xử Lý Tiếng nói để xây dựng Engine nhận diện tiếng nói theo khẩu lệnh để điểu khiển nhân vật trong game Mê cung (Maze). Từ đó, đưa ra các ý tưởng nhiều triển vọng trong việc ứng dụng vào lĩnh vực Robotics.

[![Video mô tả chung](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/174885408-499e0705-7a24-4cd1-8eb7-6caf06d2dc62.mp4)

## 2. Mô tả chức năng của ứng dụng
### a. Giao diện, chức năng Game và chuyển động

[![Chức năng](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/174885979-921cb758-24d7-48c5-bd8a-93f61356b322.mp4)

- Game được xây dựng với nhân vật gọi là Agent.
- Game được xây dựng với Graphic 2D, mỗi màn chơi là một mê cung có kích cỡ 24 cột và 15 hàng.
- Agent có thể có 4 quyết định di chuyển trong màn chơi là lên, xuống, phải trái.
- Agent không thể đi qua chướng ngại vật là những bức tường bằng gạch.
- Agent phải tìm những con đường dẫn tới đích để có thể chiến thắng màn chơi, trong đó, có những con đường sẽ dẫn tới ngõ cụt.
- Người chơi có thể chọn màn chơi theo ý muốn theo mức độ khó tăng dần.
- Người chơi có thể chọn 1 trong 2 chế độ chơi, tuy nhiên chế độ 2 nhận diện tiếng nói trong realtime có phần chưa được ổn định.

### b. Nguyên Lý Điều khiển Agent

**mode 1**

[![Controller](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/174886054-0e59e198-8c45-43c1-a25d-aa60be0dda6f.mp4)

**mode 2**

[![Controller](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/175019803-1ce34595-6939-4ffd-b1e7-a09369165839.mp4)

- Mọi hành động của Agent trong màn chơi sẽ chỉ được điều khiển bằng tiếng nói với các khẩu lệnh như **"Lên", "Xuống", "Trái", "Phải"**.
- Để điều khiển bằng tiếng nói trong chế độ 1 (Thuật toán đơn giản), người chơi sẽ nhấn phím tắt **SPACE** để đọc khẩu lệnh. Nếu trong **1.5** giây sau khi nhấn **SPACE** người chơi không đọc khẩu lệnh nào thì Agent sẽ không có hành động.
- Để điều khiển bằng tiếng nói trong chế độ 2 (Thuật toán học sâu), người chơi sẽ chỉ cần đọc khẩu lệnh và đợi Agent thực hiện xong. Người chơi không đọc khẩu lệnh nào thì Agent sẽ không có hành động, một số hành vi của Agent sẽ bị trễ nếu đọc quá nhanh.
- Hành vi của Agent có thể không được như mong muốn khi người chơi đọc khẩu lệnh, điều này phụ thuộc vào nhiều yếu tố: Môi trường có nhiều tiếng ồn - tạp âm, môi trường thu âm không đủ tốt (chất lượng của microphone, âm lượng chỉnh trên máy tính), Ngữ nghĩa logic của Speech Engine cũng chưa đủ tổng quát để có thể cover được hết toàn bộ âm sắc, năng lượng của toàn bộ loài người.
- Sau **1.5 giây recorded** với chế độ 1 hoặc **Real Time** với chế độ 2, Speech Engine sẽ xử lý khẩu lệnh được nhận vào để đưa ra quyết định hành vi cho Agent.

## 3. Mô tả về dữ liệu

[![Data Description](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/174886123-281ee8cd-4220-4c64-a924-8bf795f99101.mp4)

- Dữ liệu huấn luyện được lấy trực tiếp từ các file thu và gán nhãn khẩu lệnh âm thanh của 10 người khác nhau trong course Xử Lý tiếng nói. Các khẩu lệnh ban đầu gồm có tập hợp các từ đơn: "lên", "xuống", "trái", "phải", "A", "B", "nhảy", "bắn", tuy nhiên trong phạm vi dự án này chỉ trích lọc để sử dụng với 4 từ đơn là **"Lên", "Xuống", "Trái", "Phải"**.
- Tổng kích cỡ của dữ liệu là 4811 mẫu, tuy nhiên, để áp dụng vào thực tế ứng dụng thì không thể dùng toàn bộ các mẫu mà chỉ sử dụng một số lượng mẫu nhất định để đảm bảo hiệu suất xử lý cho ứng dụng trong chế độ 1 (DTW).
- Với chế độ 2 (Dùng mạng học sâu) thì ta chỉ cần huấn luyện bộ trong số rồi save checkpoint với keras.
- Dữ liệu trong quá trình chạy ứng dụng ở chế độ 1 sẽ được thu trong 1.5 giây và qua các bước xử lý giống như xử lý trên notebook DTW để trả về khẩu lệnh hành vi cho Agent.
- Dữ liệu trong quá trình chạy ứng dụng ở chế độ 2 sẽ được thu realtime và qua các bước xử lý giống như xử lý trên notebook NN để trả về khẩu lệnh hành vi cho Agent.
- Dữ liệu cho phần huấn luyện mô hình mạng neurals sẽ được padding zeros đều vào đầu và đuôi tín hiệu. Tương tự với phần nhận diện.

## 4. Mô tả phương pháp sử dụng trong core (Speech Engine)

**Xử lý dữ liệu và mode 1: Dynamic Time Warping**

[![Speach Engine](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.png)](https://www.youtube.com/watch?v=ZdeAOv02dZU)

**Xử lý dữ liệu và mode 2: Mạng Học Sâu**

[![Speach Engine](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.png)](https://www.youtube.com/watch?v=_YcUxt5j_p0)

### a. Trong nghiên cứu notebook
#### a.1. Xử lý tín hiệu âm thanh
- Tín hiệu âm thanh được kéo về từ google drive. Trong notebooks có mã nguồn đọc các tệp âm thanh bằng librossa, khoang vùng các đoạn thể hiện từ đơn từ file .txt nhãn. file .txt nhãn chứa thông tin về thời gian bắt đầu, thời gian kết thúc của chuỗi tín hiệu thể hiện 1 từ đơn kèm theo cả nhãn của nó.
- Tín hiệu được đọc vào sẽ có dạng mảng, trong đó, mỗi phần tử là giá trị của 1 frame. Để xác định được frame index sau đó đưa vào lưu trữ ta sẽ sử dụng công thức sau:

$$\begin{align} start_{frame} = \big\lfloor start_{time} \times samplingrate \big\rfloor \end{align}$$

$$\begin{align} end_{frame} = \big\lfloor end_{time} \times samplingrate \big\rfloor + 1 \end{align}$$

$$Sampling Rate = 22050$$

$$Frame Size = 2048$$

$$Hop Size = 512$$

#### a.2. Trích chọn đặc trưng MFCCs
**Code baseline của phần này nằm trong file DTW_Validation.ipynb hoặc NN_Validation.ipynb tại thư mục ../Material/**

- Đầu tiên ta sẽ lấy tín hiệu ban đầu để scale lại về center, sau đó sẽ làm dẹt lại 2 đầu bằng cách nhân tín hiệu với hàm cửa sổ hann.
- Biến đổi tín hiệu thành phổ Spectrum bằng Discrete Fast Fourier Transform, Spectrum có 2 chiều là tần số $Hz$ và biên độ phổ $dB$
![Discrete Fourier Transform](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/dfft.webp)
- Mục đích tiếp theo của trích chọn là lấy được Spectral Envelopes của các dominant frequency. Gọi spectrum là $X\[k\]$ có 2 thành phần là spectral envelopes $H\[k\]$ và spectral details $E\[k\]$. Để tách được $H\[k\]$, ta cần phải lấy Log để đưa về thang Mel và lấy đi phần low frequency.

$$X\[k\] = H\[k\] * E\[k\]$$

$$\implies log(X\[k\]) = log(H\[k\]) + log(E\[k\])$$

![Spectra Envelopes](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/spectra_envelopes.webp)

- Sau đó ta áp dụng các bộ lọc Mel-Frequency Filter Banks để gộp một số dominant frequency trong một khoảng vào với nhau lấy 1 con số đại diện, trong đó các filter bank là các hàm tam giác nối chân nhau.

$$m = 2595 * log(1 + \frac{f}{700})$$

$$\begin{align} f = 700 (10^{\frac{m}{2595}} - 1) \end{align}$$

Mỗi filter bank là các phương trình có dạng:

$H_m(k) = 0$ if $k < f(m - 1)$

$H_m(k) = \frac{k - f(m - 1)}{f(m) - f(m - 1)}$ if $f(m - 1) \leqslant k < f(m)$

$H_m(k) = 1$ if $k = f(m)$

$H_m(k) = \frac{f(m + 1) - k}{f(m + 1) - f(m)}$ if $f(m - 1) < k \leqslant f(m)$

$H_m(k) = 0$ if $k > f(m + 1)$

![Mel Filter Banks](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/mel-filter-banks.webp)

- Tiếp theo trên nguyên tắc ta sẽ sử dụng Inverse Fast Fourier Transform trên logarithm của spectrum tuy nhiên thay vì thế ta sử dụng Discrete Cosine Transform (1 dạng của IFFT), sau đó lấy 12 hệ số, đầu ra của pha này là cepstrum có chiều giống như speech signal với chiều ngang là trục thời gian và chiều dọc là trục các hệ số MFCCs (MFCCs Coefficients).
- Lấy trung bình biên độ của tín hiệu ban đầu trước khi DFFT để làm đặc trưng thứ 13.
- Sử dụng phương pháp normalize bằng Ceptrals mean Vector Normalization (CMVN) bằng cách lấy 13 hệ số trừ đi trung bình của chúng.
- Tiếp tục lấy Gradient cấp 2 và cấp 3 của Vector có 13 hệ số ban đầu, ta sẽ có mẫu cuối cùng là ma trận có kích cỡ $(39, d)$ với $d$ phụ thuộc vào độ dài ngắn của mẫu tín hiệu được đưa vào. Ở đây có một điều đáng chú ý trong thực nghiệm là nếu normalize bằng Z-score sẽ cho kết quả không tốt trong phân loại.
- Vì chiều của các ma trận hệ số MFCCs sẽ khác nhau ở số cột nên ta sẽ không thể đưa vào mạng neuron trực tiếp. CMVN là phương pháp Normalize tốt nhất trong dự án này.

**Tóm tắt lại quy trình: $\text{speech signal} \rightarrow \text{spectrum} \rightarrow \text{mel-filter} \rightarrow \text{cepstral}$**

### b. Sử dụng phương pháp phân loại Dynamic Time Warping

**Code baseline của phần này nằm trong file DTW_Validation.ipynb tại thư mục ../Material/**

- Kích cỡ của bộ từ vựng phân loại là nhỏ nên Dynamic Time Warping là một phương pháp tốn ít chi phí thực hiện về thời gian và tinh chỉnh, kiểm định chất lượng.
- Có thể thấy rõ ràng trong lúc trích chọn 39 MFCCs Coefficient, các samples có thể không có cùng kích cỡ về chiều thời gian giống như nhau thậm chí ngay cả trong cùng một lớp. Ta không thể coi mọi thời gian trong đặc trưng tín hiệu có ảnh hưởng như nhau, không thể tính trực tiếp bằng norm L2. Dẫn đến một phương pháp để align từng điểm rời rạc của 2 tín hiệu, đầu ra của phương pháp này có thể là dạng 1 vector (each in 39s) hoặc quy đổi trực tiếp về L2. Tức là khi thực hiện Dynamic Time Warping, ta sẽ coi mỗi điểm dữ liệu trên 2 trục alignment là một điểm có 39s chiều ứng với 39 hệ số MFCCs.

![Dynamic Time Warping](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/DTW.png)

- Ở điểm khởi đầu, ta sẽ có 3 cách để tiến hành đi tới gióng hàng với điểm tiếp theo trên trục còn lại, tức là ta có thể đi lên trên, sang phải hoặc đi chéo. Ta sẽ lấy min distance trong 3 phương án đó. Trong lúc thực hành, dự án này đã từng thực thi phương pháp giới hạn cửa số gióng hàng, nó giống soft-margin trong SVM tuy nhiên kết quả kém khiến kế hoạch phá sản. Việc giải những tối ưu khoảng cách theo đơn vị each point by each point sẽ dẫn đến một path tối ưu để gióng hàng toàn bộ 2 samples ma trận hệ số MFCCs. Tư tưởng của thuật toán này chính là quy hoạch động với từng bài toán nhỏ là những bài toán chênh lệch 1 bước alignment đối với bài toán gốc.

![Dynamic Time Warping](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/DTW2.jpg)

- Tuy nhiên, việc tính toán Dynamic time warping với một tập alignment samples quá lớn sẽ không bảo tính hiệu quả về hiệu năng xử lý khi áp dụng thực tế, chính vì thế phải có cơ chế chọn ra n-best samples theo một số bài báo về thuật toán Dynamic Time Warping. Tức ở mỗi lớp từ vững, ta sẽ chọn ra n samples tốt có ảnh hưởng lớn đến kết quả cross validation của phân loại từ. Cụ thể trong dự án này, để chọn ra 15 samples mỗi lớp từ để đưa vào sử dụng trong thực tế, một cơ chế xếp hạng các mẫu đã được đưa ra: mỗi khi một sample trong tập training có distance phân loại bé nhất trong DTW với một sample trong tập test, nó sẽ được cộng vào $(+1)$ điểm rank point nếu có cùng nhãn, phạt $(-1.5)$ rank point nếu khác nhãn với sample trong test.

Kết quả của lần traning với policy điểm rank như trên để chọn ra 15 mẫu có ảnh hưởng nhất với kết quả phân loại $(test size = 1203)$:

**Classification report:**

              precision    recall  f1-score   support

         len       1.00      0.99      1.00       310
        phai       0.98      0.97      0.97       278
        trai       0.97      0.98      0.98       304
       xuong       1.00      0.99      1.00       311

    accuracy                           0.99      1203
   macro avg       0.99      0.99      0.99      1203
weighted avg       0.99      0.99      0.99      1203

**Confussion matrix:**

![confussion matrix with all samples](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/conf_mat_1.png)

Chọn ra 15 samples tốt nhất ở mỗi lớp từ để đánh giá lần 2:

**Classification report:**
              precision    recall  f1-score   support

         len       1.00      0.95      0.97       324
        phai       0.79      0.89      0.84       247
        trai       0.90      0.85      0.88       321
       xuong       0.98      0.98      0.98       311

    accuracy                           0.92      1203
   macro avg       0.92      0.92      0.92      1203
weighted avg       0.93      0.92      0.92      1203

**Confussion matrix:**

![confussion matrix with typical samples](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/conf_mat_2.png)

Nhận xét: Nhìn chung ta sẽ đánh đổi chất lượng có thể chấp nhận được trong bài toán phân loại để lấy được một thời gian xử lý phù hợp với thực tế ứng dụng.

### c. Sử dụng phương pháp phân loại bằng mạng học sâu

**Code baseline của phần này nằm trong file NN_Validation.ipynb tại thư mục ../Material/**

- Kiến trúc mạng: tầng đầu vào ứng với phần đệm tổng quát của tín hiệu sau khi lấy được MFCCs coefficients. (1482 nút)
- Các tầng fully connected bên trong là 512 - ReLu; dropout 0.3; 256 ReLu; 256 ReLu; dropout 0.3; 128 ReLu; 4 Softmax
- Hàm lỗi là hàm Categorical CrossEntropy và Optimizer method là Adam (Ada Grad Momentum)

Kết quả của mạng học sâu cho thấy nó cực kỳ mạnh mẽ và phù hợp với dự án khi thực hiện realtime recognition
              precision    recall  f1-score   support

           0       0.97      0.98      0.98       265
           1       0.97      0.97      0.97       228
           2       1.00      1.00      1.00       247
           3       1.00      1.00      1.00       223

    accuracy                           0.99       963
   macro avg       0.99      0.99      0.99       963
weighted avg       0.99      0.99      0.99       963

### d. Đưa Speech Engine vào ứng dụng
- Control flow của Speech Engine sẽ theo một quy trình chuẩn như sau:

**Mode 1**

![SPEECH ENGINE FLOW ACTIONs in mode 1](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/speech_engine_flow.png)

**Mode 2**

![SPEECH ENGINE FLOW ACTIONs in mode 2](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/speech_engine_flow_2.png)

## 5. Kết luận
- Speech Engine đã hoạt động một cách khá tốt trong các lần chạy thử ứng dụng chứng tỏ các sapmles điển hình ở mode 1 có tính tổng quát tốt trong thực tiễn.
- Speech Engine đã hoạt động cũng khá ổn định trong các lần chạy thử ứng dụng ở mode 2 chứng tỏ mạng học sâu có tính tổng quát tốt trong thực tiễn.
- Việc xây dựng một Speech Engine ứng dụng vào thực tế không dễ dàng, đặc biệt là với vấn đề realtime, đó cũng là một điểm thiếu sót trong ứng dụng. Ứng dụng vẫn cần một cơ chế tách luồng Threading Dispatch để có thể hoạt động ổn định hơn ở chế độ realtime.
- Các threehold để phân biệt các lớp từ với một từ ngoại lai (outlier noises) thực sự không rõ ràng, mặc dù trong dự án đã áp dụng một số ngưỡng cụ thể về cả xác suất lẫn khoảng cách tuy nhiên chúng không đem lại hiệu quả cao.
- Các phương pháp không dựa trên samples thực dụng giống DTW như mô hình HMM, Mạng NN với các bộ trọng số của nhiều tầng ẩn, Transformer trong Compiler có thể hiệu quả hơn phương pháp được áp dụng trong dự án này.
- Từ baseline của dự án có thể đưa ra những ý tưởng để áp dụng Speech Engine trong điều khiển Robotics, tuy nhiên dự án này sẽ chỉ là một phần nhỏ trong hướng phát triển đó vì khi thoát li khỏi môi trường mô phòng là các vấn đề về không gian, tầm nhìn vận hành ở môi trường thực tế của Robots.

## **Chạy thực nghiệm ứng dụng**

**Mode 1**

[![Ingame Experience mode 1](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/175027115-3bce2669-cd67-4ca1-97aa-da7acd4a4f7d.mp4)

**Mode 2**

[![Ingame Experience mode 2](https://raw.githubusercontent.com/Warlock-NTD/Maze-Game-Speech-Operation/main/Material/preview.jpg)](https://user-images.githubusercontent.com/76658438/175026207-c66b5dc7-e005-45ac-9339-3a40317e8b2e.mp4)
