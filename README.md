# web3-App 

<h2>:open_file_folder: About The Project</h2>
This is a token transfer app. <br>
In particular, in this simple simulation, you can transfer an ERC-20 token (Basil :seedling:) from an address to another. <br>
After the transaction, the transaction events will be saved in a NoSQL dabatabe as MongoDB.

<h2>🔧 Build With</h2>
 Remix <br>
 Django <br>
 Ganache <br>
 MongoDB <br>
 
<h2>:mag_right: In Detail</h2>

First of all, we are going to create our ERC-20 Token using [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol)
standard, as you can see in [Basil Token file](https://github.com/MikeMoresi/web3-App/blob/main/App/MyToken.sol) <br>
After that, on the homepage, the user can add his address, the recipient address,the amount and start the transaction. <br>
If something goes wrong an error page will appear to help to understand which is the error
