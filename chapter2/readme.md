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

## Why smart contracts 

## Summary
