# Implementing Smart Contracts Using Vyper 
许多正在学习如何编写智能合约的程序员将学习Solidity编程语言。

当与Truffle框架相结合时，Solidity形成了开发智能合约的杀手级组合。以太坊区块链上几乎所有的智能合约都是用Solidity编程语言编写的。
## Motivations behind Vyper 
寫一份聰明的契约需要一種不同的心態。 這個智慧合約的應用範圍從編寫財務應用程序到向太空發射火箭。 部署智慧合約後修復錯誤非常困難


您無法替換智慧合約，因為一旦部署了它，它就會被部署。 如果你編寫了一個函數來銷毀智慧合約，你可以銷毀它，但修復有故障的智慧合約的唯一方法是在新地址中部署一個修復了錯誤的新智慧合約，然後將這種情況傳達給所有相關方。 但你無法取代智慧合約。

Solidity的另一個功能可能會讓智慧合約變得複雜和難以閱讀，那就是修飾符，它就像一個初步功能。 以下程式碼顯示了修改器在Solidity中的使用管道：
```
modifier onlyBy(address,_account)
{
    require(msg.sender==_account,"Sender not authorized.");
    _;
}
function withdraw() public onlyBy(owner)
{
    //withdraw money;
}
```

如果我們想使用`withdraw（）`方法，智慧合約將執行
`onlyBy（）`修飾符方法。 require短語用於確保msg.sender（調用此方法）與account變數相同,作為參數發送的。 
這個例子很簡單。 你可以閱讀
程式碼眨眼之間。 然而，考慮到這些功能
由許多行分隔，或者甚至在另一個檔案中定義。 程式師
傾向於忽略onlyBy（）方法的定義。

函數重載是程式設計語言中最强大的功能之一。 這是一個允許您發送不同參數以獲得不同函數的功能，如以下程式碼所示：
```
function flexable_function(uint _in) public {
    other_balance = _in;
}
function flexible_function(uint,_in,uint _in2) public{
    other_balance = _in + _in2;
}
function flexible_function (uint _in,uint _in2, uint _in3) public {
    other_balance = _in + _in2 - _in3;
}
```
這些聰明的人决定創造一種新的程式設計語言
比Solidity更簡單。 Python是他們的主要靈感來源，因為
這種程式設計語言源自Python。 此程式
這種語言被稱為Vyper。 在Vyper中，繼承、函數等特性
重載、修飾符和許多其他內容都被删除了。 的創建者
Vyper程式設計語言認為，删除這些功能可以
讓智慧合約的開發變得更容易。 重要的是，它還使
程式碼更易於閱讀。 程式碼讀起來比寫起來多得多。 與所有
在這些因素中，他們希望程式師在
使用Vyper程式設計語言創建智慧合約。


## Installing Vyper 
`pip install vyper`
使用vyper進行安裝確認
`vyper --version`
然後運行
`vyper hello.vy`

這是智慧合約的位元組碼。 請記住，要部署智慧合約，需要位元組碼，但要訪問智慧合約，則需要abi。 那麼你是怎麼得到abi的呢？ 您可以通過運行以下命令來執行此操作：
`vyper -f json hello.vy`
還可以一起二進制和abi一起返回
`vyper -f json,bytecode hello.vy`

### Deploying a smart contract to Ganache 
但讓我們用一種熟悉的方法來使用truffle 

```
mkdir hello_project
hello_project/
truffle init

```
修改`hello_project/build/contracts`裡面的
然後用編譯過程輸出的abi或json填充abi欄位，用編譯過程的位元組碼輸出填充位元組碼欄位。 您需要用雙引號引用位元組碼值
引號。
不要忘記在abi欄位和位元組碼欄位之間加逗號。 這將為您提供類似於以下內容的內容：


然後，您可以通過在migrations/2_deploy_hello.js中創建一個新檔案來創建一個遷移檔案來部署此智慧合約，如下所示

使用了pipinstall但是報錯

```
dyMBP:Blockchain danyow$ vyper --version
bash: vyper: command not found
```
實在不行了上docker
> https://docs.vyperlang.org/en/stable/installing-vyper.html
```
docker run -v $(pwd):/code/ -it --entrypoint /bin/bash vyperlang/vyper
```
進去了然後報錯
```
blockchain) dyMBP:Blockchain danyow$ docker run -v $(pwd):/code/ -it --entrypoint /bin/bash vyperlang/vyper
root@52c0186fda65:/code# ls
chapter1  chapter2  chapter3  readme.md
root@52c0186fda65:/code# vyper chapter3/hello.vy 
Error compiling: /code/chapter3/hello.vy
vyper.exceptions.VyperException: Compilation failed with the following errors:

FunctionDeclarationException: Unknown decorator: public
  contract "/code/chapter3/hello.vy:11", function "say_hello", line 11:1 
       10
  ---> 11 @public
  ---------^
       12 def say_hello()-> bytes[32]:


FunctionDeclarationException: Unknown decorator: public
  contract "/code/chapter3/hello.vy:7", function "change_name", line 7:1 
       6
  ---> 7 @public
  --------^
       8 def change_name(new_name:bytes[24]):


FunctionDeclarationException: Unknown decorator: public
  contract "/code/chapter3/hello.vy:3", function "__init__", line 3:1 
       2
  ---> 3 @public
  --------^
       4 def __init__():


UnknownType: No builtin or user-defined type named 'bytes'. Did you mean 'bytes1', or maybe 'bytes2'?
  contract "/code/chapter3/hello.vy:1", line 1:13 
  ---> 1 name: public(bytes[24])
  --------------------^
       2

```


## Creating a smart contract with Vyper
> chapeter3/hello.vy
報錯
`root@52c0186fda65:/code# vyper chapter3/hello.vy 
Error compiling: /code/chapter3/hello.vy
AttributeError: type object 'BytesT' has no attribute 'typ'
`


## Deploying a smart contract to Ganache
> 因為要用到vyper裡面的東西 fail


## Going deeper into Vyper 
**代碼解析**
`name:public(bytes[24])`
The array of bytes is basically a string. The variable called name has a type of
array of bytes or string. Its visibility is public. If you want to set it to private,
then just omit the public keyword, as follows:
`name:bytes[24]`
 
### Data types
> 創建donation.vy 
**代碼解析**

- strcut:
  第一個稱為結構。 Vyper中的結構就像另一種程式設計語言中的結構； 它是不同資料類型的容器。 您可以按以下管道訪問其成員：
- wei:
  我們將要瞭解的第二種資料類型是
uint256（wei）。 這是指可以容納的特定數量的乙醚。 如您所知，1乙太是1000000000000000000wei（18個零）。 要保存這麼大的數量，需要特定的資料類型

- Timestamp:
- Address:
  The fourth one is the address data type. This is designed to
hold the address value (such as 0xdCad3a6d3569DF655070DEd06cb7A1b2Ccd1D3AF)



### Withdrawing ethers
```
@external
def withdraw_donation():
    assert msg.sender == self.donatee 
    send(self.donatee,self.balance)
```
這裡，self.lance表示在該智慧中累積的所有醚
契约 send短語是一個內寘函數，用於將錢轉移到第一個
參數，在本例中為受贈人。
囙此，讓我們在Truffle控制台中測試這個智慧合約。 確保您更改
方法中的地址到智慧合約的地址。 你可以得到
它使用truffle migrate命令，如下所示：

## Interacting with other smart contracts 
> 結合vy和truffle
結合`hello.vy`和`hello_project/migrations/2_deploy_hello.js`
```
var Donation = artifacts.require("Hello");
module.exports = function(deployer)
{
    deployer.deployer(Hello);
}
```
再次編譯hello.vy檔案以獲得介面和位元組碼。 打開我們的契约JSON檔案，`build/contents/Hello.json`檔案。 擦除所有
內容，並將其替換為以下程式碼：
```
```
你必須為你的智慧合約命名，因為這一次，你
將部署兩個智慧合約。 如果你不給你的聰明人起個名字
契约，它將有一個默認名稱，契约。 如果你只是
想要部署一個智慧合約。

Then, for your donation.vy, edit it, and add the following lines of code
(highlighted in bold) to the code file (refer to the code file in the following
GitLab link for a complete code file of donation.vy at https://gitlab.com/arjunask
ykok/hands-on-blockchain-for-python-developers/blob/master/chapter_03/donation.vy):
