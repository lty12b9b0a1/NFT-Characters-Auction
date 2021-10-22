// SPDX-License-Identifier: GPL3.0
pragma solidity 0.8.9;

contract Lottery{
    address payable public manager;
    address payable[] public players;
    uint256 public round;
    address payable public winner;

    constructor() public {
        manager = payable(msg.sender);
    }

    //1.���Ʊ��ÿ��ֻ��Ͷ1ETH
    function play() public payable {
        require(msg.value == 0.1 ether);
        //2.�Ѳ����߼�������
        players.push(payable(msg.sender));
    }

    modifier onlyManager{
        require(msg.sender == manager);
        _;
    }

    function getPlayersCount() public view returns (uint256){
        return players.length;
    }

    function draw() public onlyManager {
        //��������ʱ�䡢�����Ѷȡ������������������
        bytes memory v1 = abi.encodePacked(block.timestamp, block.difficulty, players.length);
        bytes32 v2 = keccak256(v1);
        uint256 v3 = uint256(v2);
        uint256 index = v3 % players.length;
        //��¼��һ���н���
        winner = players[index];
        //ת��
        uint256 money = address(this).balance * 90 / 100;
        uint256 money2 = address(this).balance - money;
        winner.transfer(money);
        manager.transfer(money2);
        //����������������һ����ղ����
        round++;
        delete players;
    }

    function refund() public onlyManager {
        for (uint256 i = 0; i < players.length; i++) {
            players[i].transfer(0.1 ether);
        }
        round++;
        delete players;
    }
    
    function getPlayers() public view returns(address payable[] memory){
        return players;
    }

    function getBalance() public view returns (uint256){
        return address(this).balance;
    }

}