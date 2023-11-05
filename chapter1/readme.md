# Introduction to Blockchain programming 

## The rise of cryptocurrency and blockchain 
> cryptocurrency 虛擬貨幣

区块链开始被用作一种没有中间商的支付解决方案，
即比特币。然后，人们发现区块链还有其他一些
有趣的属性。首先，它是透明的，这意味着人们可以
对其进行审计，以检查是否存在洗钱行为。
其次，它在一定程度上为用户提供了隐私，可以用来
避免剖析。
然后，在以太坊发布后，人们突然对
如何在现实生活中应用区块链。从创建要表示的令牌
对某物的所有权，如自治组织或付款
拥有完全隐私，可以访问无法复制的数字资产（与MP3不同
文件）。

## Blockchain technology
Blockchain = 它是一個僅附加的資料庫，由通過雜湊連結的塊組成。

在這裡，每個區塊都包含許多由加密技術保護的參與者之間的價值轉移交易（但也可能是其他交易）； 持有相同資料庫的許多節點之間的一致性决定了下一個要附加哪個新塊。

總結概括為 是個`append-only`數據庫


那麼，您可以在這個僅追加的資料庫中放入什麼呢？ 這取決於加密貨幣。 

為了更清楚，我們將所有這些事務放入塊中，然後將它們附加到僅追加資料庫中。 除了事務清單之外，我們還在這個塊中存儲其他內容，例如將塊附加到僅附加資料庫的時間、目標的難度（如果您不知道這一點，請不要擔心）和父級的雜湊（我稍後將對此進行解釋），以及其他許多內容。



既然你瞭解了區塊鏈的區塊元素，讓我們看看
鏈條元件。 如前所述，除了
事務，我們還將父級的雜湊放入塊中。 但現在，讓我們
使用簡單的ID來訓示父項，而不是使用雜湊。 父id為
只是前面的塊id。在這裡，想想堆棧。 一開始
沒有阻塞。 相反，我們放置了區塊A，它有三個交易：
事務1、事務2和事務3。 由於區塊A是第一個
塊，它沒有父級。 然後，我們將塊B應用於塊A，它包括
兩個事務：事務4和事務5。 B區不是第一個
區塊鏈中的一個。 囙此，我們將塊B中的父節設定為
塊A id，因為塊A是塊B的父塊。然後，我們將
區塊鏈中的區塊C，有兩個交易：交易6和
交易7。


用數據庫實現一下，在過去你說你喜歡貓而現在你不喜歡貓，但是過去你喜歡貓的事實沒有變
```python
class Block:
    id = None 
    history = None 
    parent_id = None 
block_A = Block()
block_A.id = 1 
block_A.history = 'Nelson likes cat'

block_B = Block()
block_B.id = 2
block_B.history = 'Marie likes dog'
block_B.parent_id = block_A.id 

block_C = Block()
block_C.id = 3
block_C.history = 'Sky hates dog'
block_C.parent_id = block_B.id
```


### Signing data in blockchain 
在區塊鏈中，我們使用兩個金鑰對數據進行簽名，驗證消息並保護其不被未經授權的用戶更改。 這兩把鑰匙如下
- private key 私密金鑰
- public key 公開金鑰
私密金鑰的秘密是保密的，它不為公眾所知。 另一方面，您讓公開金鑰在公共場合發佈。 你告訴所有人，嘿，這是我的公開金鑰。
讓我們生成私密金鑰。 要做到這一點，我們需要openssl軟件。 你可以
通過執行以下操作進行安裝：
`sudo apt-get install openssl`
生成private key 
`openssl genrsa -out nelsonkey.pem 1024`
生成public key
`openssl rsa -in nelsonkey.pem -pubout > nelsonkey.pub`

查看python腳本去簽署信息
> verify_message.py
 

讓我們來看看一個案例，在這個案例中，瑪麗試圖用一個名為證偽_消息.py的腳本來偽造事實。瑪麗試圖將納爾遜討厭的猫放入歷史資料庫，如下所示：
> falsify_message.py


### From linked list to blockchain
就這樣，歷史已經改變了。 我們可以通過每天在區塊中記錄所有歷史來避免這種作弊管道。
囙此，當Nelson更改資料庫時，我們可以將今天區塊鏈中的數據與昨天區塊鏈中數據進行比較。 如果情况不同，我們可以確認發生了可疑的事情。 這種方法可能奏效，但讓我們看看是否能想出更好的方法。


讓我們將連結清單陞級到區塊鏈。 為此，我們在Block類中添加一個新内容，它是父級的雜湊：
> block.py

大概講的是，如果要更改歷史的話，就要改parent，parent_hash根據你的改變而改變。

## Cryptography
區塊鏈最流行的用途是創建加密貨幣。 由於加密貨幣中有cryptocurrency一詞，你會認為你需要掌握
密碼學，以成為區塊鏈程式師。 這不是真的。 關於密碼學，您只需要瞭解兩件事：
- Private key and public key (asymmetric cryptography)
- Hashing

不需要知道如何設計雜湊演算法或私密金鑰公開金鑰算灋。 你只需要學會怎麼使用

public key，private key是用來分散帳戶。
在常規的應用程式中，user用戶擁有帳號和密碼來進入帳戶，同理擁有public key和private key讓user在分散管理中擁有帳戶。

對於hash函數，可以通過輸入，得到輸出，但沒辦法通過輸出得到輸入，用數學可以標示為
$$
f(x,y) \geq  x+y
$$

### Symmetric and asymmetric cryptography
對稱加密在發送方和接收方之間使用相同的金鑰。 此金鑰用於對消息進行加密和解密。

非對稱密碼學是另一種野獸。 有兩個金鑰：一個公開金鑰和一個私密金鑰。 它們之間有著特殊的數學關係。 如果使用公開金鑰對消息進行加密，則只能使用私密金鑰對其進行解密。 如果您使用私密金鑰加密消息，
您只能使用公開金鑰對其進行解密。 公開金鑰和私密金鑰之間沒有像對稱金鑰那樣的直接關係（加减相同的數位）


與對稱密碼學相比，非對稱密碼學使人們能够安全地進行通信，而無需首先交換金鑰。

## the hashing function
簡單了解一下hash
```powershell
>>> import hashlib
>>> hashlib.sha256(b"hello").hexdigest()
'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

```
無論輸入是多長長度的，固定返回64位置，當輸入相同，輸出也會相同。

### Proof of work
So, we have three participants in this case: Nelson, Marie, and Sky. But
there is another type of participant too: the one who writes into the
blockchain is called—in blockchain parlance—the miner. In order to put the
transaction into the blockchain, the miner is required to do some work first.

我們需要在block.py添加新的塊，再添加block之前，我們首先要求礦工做一些拼圖工作。


我們序列化該塊，並要求礦工應用一個額外的字串，當該字串附加到該塊的序列化字串時，如果進行了雜湊處理，則會顯示前面至少有五個零的雜湊輸出。
> block_v2.py

## consensus 一致的意見
正如我們所看到的，散列函數使篡改歷史變得困難，但並不太困難。 即使我們有一個由1000個塊組成的區塊鏈，用最近的電腦更改第一個塊的內容並更改其他塊上的999個父雜湊也是微不足道的


礦工將從Sherly那裡選擇區塊鏈，而不是他們之前保存的區塊鏈，其中包含Sherly喜歡鯊魚的歷史。 囙此，雪麗已經能够改變歷史。 這就是我們所說的雙重支出攻擊

我們可以通過工作證明（添加區塊的激勵措施）來防止這種情況的發生。 我們在本章早些時候解釋了工作證明，但我們還沒有解釋激勵制度。 激勵意味著如果礦工成功
在區塊鏈中添加一個新的區塊，系統會給他們數位獎勵。 我們可以將其集成到程式碼中，如下所示：



如果雪麗想改變歷史（通過更換一些區塊），她需要
花一些資源在短時間內解决四個難題。 時代
她完成了這項工作，大多數礦工都會保留區塊鏈
可能添加了更多的區塊，使其比Sherly的區塊鏈更長。
之所以會出現這種情況，是因為大多數礦工都想獲得我們在
以最有效的管道。 要做到這一點，他們會得到一個新的
候選區塊，努力在工作證明中找到答案，然後
儘快將其添加到最長的鏈中。 但是，他們為什麼要
把它加到最長的鏈上，而不是另一個鏈上？ 這是因為它
他們的獎勵。


**Consequently, the reward would be taken away from the miner. The longest chain attracts the most miners anyway**


## Coding on the blockchain 
：比特幣只是用來匯款的，但你可以在乙太坊上創建一個程式。 該程式可以是代幣、拍賣或託管，以及許多其他東西。 但這是半個事實。 你也可以在比特幣上創建一個程式

舉例來說，進行比特幣交易的腳本類似於
`What's your public key? If the public key is hashed, does it equal Z? If yes,
could you provide your private key to prove that you own this public key?`

但它可能有點花哨。 假設您需要四個授權簽名中的至少兩個簽名才能解鎖此帳戶； 你可以用比特幣腳本做到這一點。 創造性思維，你就能想出這樣的東西
`This transaction is frozen until 5 years from now. Then business will be as usual,
that the spender must provide public key and private key.`

但比特幣腳本是用一種簡單的程式設計語言創建的，
甚至不能迴圈。 它是基於堆棧的。 所以，你放指令：hash
公開金鑰，檢查簽名，並檢查當前時間。 然後，它會
在比特幣節點上從左到右執行。'

有的人不滿意循環死板，
有些人不滿足於這種限制，於是乙太坊應運而生。 您在乙太坊區塊鏈上配備的程式設計語言比程式設計複雜得多
比特幣中的語言（有一段時間或用於構造）。 從科技上講，你可以創建一個在乙太坊區塊鏈中永遠運行的程式。


囙此，人們喜歡區分比特幣（BTC）和乙太坊（ETH）的貨幣。 BTC就像數位黃金。 ETH就像石油和瓦斯。 如果我們用這個比喻的話，兩者都是有價值的。 但是，你可以利用石油和瓦斯來創造一個全新的世界，比如通過製造塑膠、燃料等。另一方面，除了製作珠寶之外，你能用黃金做的事情非常有限。

### Other types of blockchain programmers 
本章旨在讓您直觀地瞭解區塊鏈的工作原理。 然而，它並不是一個完整的工作範圍。 我的解釋與比特幣（甚至乙太坊）的工作原理有很大不同。 乙太坊不使用SHA-256進行雜湊； 它通常使用Keccak-256算灋。 在我們的案例中，我們只放了一個

區塊鏈程式設計可能意味著你正在努力改善比特幣的狀態，或創建比特幣的分支，如比特幣現金。 您需要C++和Python。 如果你正在創建一個比特幣分叉，比如比特幣黃金，你需要更深入地研究密碼學。 在Bitcoin Gold中，開發人員將工作證明雜湊函數從SHA-256更改為Equihash，因為Equihash具有ASIC抗性。 ASIC電阻意味著您無法創建特定的電腦來進行雜湊處理。 你需要一臺帶有GPU的電腦來執行Equihash雜湊函數，但本書不會討論這一點

三個語言`Go,c++,python`


## Summary
