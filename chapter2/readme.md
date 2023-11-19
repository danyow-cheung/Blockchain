# Smart Contract Fundamentals 
在本章中，我們將探討智慧合約的基礎知識。 在比特幣中我們存儲價值，在乙太坊中我們存儲程式碼。 我們存儲在乙太坊中的程式碼被稱為智慧合約。 智慧合約是一種不可信的程式碼，
這意味著程式碼的完整性受到算灋和密碼學的保護

這為創建許多類型的應用程序打開了可能性，如透明的數位代幣、無信任的眾籌、安全的投票系統和自主組織

## Installing an Ethereum development env
use the Vyper programming language to develop a smart contract

### node.js
.pkg 解決

### truffle and solidity
Truffle is a development framework for developing a smart contract with Solidity.

which including a console application to interact with the blockchain network and the development
blockchain software. 

On top of that, with Truffle, you get the Solidity compiler as well.

一些配置命令行
```
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
source ~/.bash_profile # mac文件的不同
npm install -g truffle
truffle version

```

### Ganache 
Ganache是一個私有的開發乙太坊網絡，您只能在乙太坊開發階段使用。 Truffle框架已經包括乙太坊區塊鏈網絡，其目的與Ganache相同。
兩者的區別在於Ganache有一個前端GUI和一個更用戶友好的介面。

你需要花錢才能推出乙太坊區塊鏈中的智慧合約。 

直接使用.dmg完成安裝


## Writing a smart contract
進入某個文件夾，然後`truffle init`
```

Starting init...
================

> Copying project files to /Users/danyow/Desktop/self-learning/BlockChain/chapter2/first_contract

Init successful, sweet!

Try our scaffold commands to get started:
  $ truffle create contract YourContractName # scaffold a contract
  $ truffle create test YourTestName         # scaffold a test

http://trufflesuite.com/docs
```
您通常将智能合约的源代码合并到`contracts`文件夹中。`migrations`文件夹保存智能合约部署中使用的文件，`test`文件夹保存测试文件。您可以在`truffle-config.js`文件中配置智能合约部署设置。我们将创建第一个智能合约，并使用以下代码将其命名为`donation.sol`：

> 需要把`donation.sol` 放在 `contracts`文件夾下


let's compile this smart contract written in Solidity to Ethereum bytecode and an application binary interface (abi). To do this, we will run the following command in the Truffle project directory:
`truffle compile`
結果會放在`build/contracts`文件夾，命名為`Donation.json`


## Developing a smart contract to Ethereum blockchain
以下是使用Truffle将智能合约部署到以太坊区块链的步骤：
1. 寫一個`migration`腳本
    創建一個新的文件`migration/2_deploy+donation.js`
    
2. 發送`Ganache`
    執行Ganache
    您将从Ganache屏幕中注意到的一件事是RPC SERVER，
    位于http://127.0.0.1:7545.这是您的以太坊区块链位于Truffle项目目录中的位置

3. 編輯`Truffle configuration file`
    将其删除，并将以下代码行添加到truffle-config.js文件中：

4. 執行`migration`腳本
   `truffle migrate`返回輸出
   ```
   Compiling your contracts...
    ===========================
    > Everything is up to date, there is nothing to compile.


    Starting migrations...
    ======================
    > Network name:    'development'
    > Network id:      5777
    > Block gas limit: 6721975 (0x6691b7)


    2_deploy_donation.js
    ====================

    Deploying 'Donation'
    --------------------
    > transaction hash:    0x8e29f587ad12a8abf3810e1012b5a1d69263c92be755c96a69a6eb4c2f8aa662
    > Blocks: 0            Seconds: 0
    > contract address:    0x97F11C4a43897e03078a8CD6706cF922F5a5E90E
    > block number:        1
    > block timestamp:     1699673209
    > account:             0x461F47Cbe68eD1DA422bC66Cb7Ea8301977FB9a0
    > balance:             99.998763632875
    > gas used:            366331 (0x596fb)
    > gas price:           3.375 gwei
    > value sent:          0 ETH
    > total cost:          0.001236367125 ETH

    > Saving artifacts
    -------------------------------------
    > Total cost:      0.001236367125 ETH

    Summary
    =======
    > Total deployments:   1
    > Final cost:          0.001236367125 ETH

   ```

## Interacting with smart contracts
> env: /Users/danyow/Desktop/self-learning/BlockChain_env
> 

To interact with your smart contract that resides in Ethereum blockchain,
execute this command inside your Truffle project directory:
`truffle console`
在終端進行輸入
```
Donation.deployed().then(function(instance) { return instance.useless_variable.call(); });
```

報錯了
```
Error: Returned values aren't valid, did it run Out of Gas? You might also see this error if you are not using the correct ABI for the contract you are retrieving data from, requesting data from a block number that does not exist, or querying a node which is not fully synced.
```
不會解決跳過了。

，Truffle控制台使用回调的概念，在回调上异步执行对智能合约对象的访问。
Truffle控制台中的此语句在执行回调之前立即返回。

在回调函数中，您将接受智能合约实例作为`instance`参数。然后，我们可以从这个实例参数访问我们的`useless_variable`变量。然后，为了检索值，我们必须对该变量执行调用方法。

Truffle框架将使用Donation.json文件中定义的abi来了解智能合约中可用的接口。回想一下
您可以在智能合约中定义uselessvariable，并在构造函数（或初始化）函数中将其设置为Donation字符串。以这种方式读取公共变量是免费的；它不需要任何以太币，因为它存储在区块链中

再輸入
```
Donation.deployed().then(function(instance) { return instance.change_useless_variable("sky is blue", {from: "0xc98abE91356000e656d53b1edFC716369b37c524" }); });
```
返回 
```
{
  tx: '0x729429697878bcfd9df9be6739133525f568a14aa77d312052f73227a49dc1d1',
  receipt: {
    transactionHash: '0x729429697878bcfd9df9be6739133525f568a14aa77d312052f73227a49dc1d1',
    transactionIndex: 0,
    blockNumber: 2,
    blockHash: '0x9e3276b82c9a902ccc17932cb2e907fba0dc60f6bcbe442d20c7361f1f9e3fbb',
    from: '0xc98abe91356000e656d53b1edfc716369b37c524',
    to: '0xf725b914e004cda152a0799c1411698bb73998e8',
    cumulativeGasUsed: 29789,
    gasUsed: 29789,
    contractAddress: null,
    logs: [],
    logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    status: true,
    effectiveGasPrice: 3277546336,
    type: '0x2',
    rawLogs: []
  },
  logs: []
}

```
### Sending ether to smart contracts 
现在，让我们向智能合约发送一些以太币。让我们使用第二个帐户。第二个帐户想使用智能捐赠5以太币
合同如下：
```
Donation.deployed().then(function(instance) { return instance.donate({ from: "0xc98abE91356000e656d53b1edFC716369b37c524", value:5000000000000000000 }); });
```
返回
```python
truffle(development)> Donation.deployed().then(function(instance) { return instance.donate({ from: "0xc98abE91356000e656d53b1edFC716369b37c524", value:5000000000000000000 }); });
{
  tx: '0x7879654a56ff6fb6dac2b04d86553ab4a30c99ff8fc476ea37fd5522c733bfdc',
  receipt: {
    transactionHash: '0x7879654a56ff6fb6dac2b04d86553ab4a30c99ff8fc476ea37fd5522c733bfdc',
    transactionIndex: 0,
    blockNumber: 3,
    blockHash: '0x4127c5a039c4b834d3902c4197999bd5ebf20a1ce2b8558bee94f781992be423',
    from: '0xc98abe91356000e656d53b1edfc716369b37c524',
    to: '0xf725b914e004cda152a0799c1411698bb73998e8',
    cumulativeGasUsed: 65551,
    gasUsed: 65551,
    contractAddress: null,
    logs: [],
    logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    status: true,
    effectiveGasPrice: 3181214485,
    type: '0x2',
    rawLogs: []
  },
  logs: []
}
```
為什麼value會有那麼多零的原因是
当你在以太坊区块链中转账时，你必须使用最低的货币单位（类似于从
美元转换为美分），


让我们使用第一个帐户提取：
```
Donation.deployed().then(function(instance) { return instance.receive_donation({ from: "0x06f4f7DD1Fd8edFE119417817890611E2710Cbe9" });});
```
返回
```
ndefined
truffle(development)> Donation.deployed().then(function(instance) { return instance.receive_donation({ from: "0x06f4f7DD1Fd8edFE119417817890611E2710Cbe9" });});
{
  tx: '0x1c07e3b5e16f6f215a9518951ced2346b106496c03368ff866dfe6fb459e9a76',
  receipt: {
    transactionHash: '0x1c07e3b5e16f6f215a9518951ced2346b106496c03368ff866dfe6fb459e9a76',
    transactionIndex: 0,
    blockNumber: 4,
    blockHash: '0x66639ebdbf233c18e58acf4acd032fce213ab877452eda0fd036a20d29de3af4',
    from: '0x06f4f7dd1fd8edfe119417817890611e2710cbe9',
    to: '0xf725b914e004cda152a0799c1411698bb73998e8',
    cumulativeGasUsed: 32794,
    gasUsed: 32794,
    contractAddress: null,
    logs: [],
    logsBloom: '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    status: true,
    effectiveGasPrice: 3097723433,
    type: '0x2',
    rawLogs: []
  },
  logs: []
}
```
## Why smart contracts 
智能合约能做什么传统程序（普通的网络应用程序）做不到的？当涉及到更改网络上程序中变量的值时，我们可以使用远程过程调用。

事实上，一个普通的web应用程序可以做智能合约所能做的一切，但速度更快、更便宜。关键的区别在于区块链解决方案可以是不可信的。这意味着您可以信任程序本身，但不能信任操作员。

## Summary
