pragma solidity ^0.8.7;

import 'https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol';


contract Basil is ERC20{
    address owner;
    constructor() ERC20('Basil','BIL'){
        _mint(msg.sender,10000*10**18);
        owner=msg.sender;
    }
}
