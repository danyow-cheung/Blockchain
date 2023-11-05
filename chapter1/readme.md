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
 
## Cryptography


## the hashing function

## consensus 

## Coding on the blockchain 

## Summary
