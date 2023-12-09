# RSA_decrypt
Alice使用的RSA密码体制，有以下事项需要说明：
1. 模数𝑁=𝑝𝑞规模为1024比特，其中𝑝，𝑞为素数；
2. 每次加密最多8个明文字符；
3. 明文超过8个字符时，对明文分片，每个分片不超过8个字符；
4. 分片明文填充为512比特消息后再进行加密，填充规则为高位添加64比特标志位，随后加上32比特通信序号，再添加若干个0，最后64比特为明文分片字符对应的ASCII码（注：填充方式参见加密案例，但注意每次通信的标志位可能变化）；
5. 分片加密后发送一个加密帧数据，帧数据文件名称为FrameXX，其中XX表示接收序号，该序号不一定等于通信序号；
6. 帧数据的数据格式如下，其中数据都是16进制表示，结构如下:
`1024bit模数N|1024bit加密指数e|1024bit密文`
7. 由于Alice初次使用该软件，可能会重复发送某一明文分片。

请您尝试恢复每个帧数据的p和q，以及明文M

每个密文的格式：  1024bit模数 N | 1024bit加密指数 e | 1024bit密文

请尝试用各种分析方法恢复明文 ( 可以先分解N再恢复明文，也可以不分解直接恢复明文)

明文
My secre
t is a f



instein.
 That is
 "Logic 
will get
 you fro
m A to B
. Imagin