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


## Creating a smart contract with Vyper

## Deploying a smart contract to Ganache

## Going deeper into Vyper 

## Interacting with other smart contracts 
