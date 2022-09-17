from brownie import Contract, accounts, interface
from brownie_tokens import MintableForkToken

def getWETH(amount):
    WETH_ADDRESS ='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    WETH = MintableForkToken(WETH_ADDRESS)
    WETH._mint_for_testing('0x04F14CF56f56cAB0c10be862c78F2670f4FBD121', amount)

# def approve_ERC20(amount, to, erc20_address, myaccount):
#     erc20 = interface.IERC20(erc20_address)
#     tx_hash = erc20.approve(to, amount, {'from': myaccount})
#     tx_hash.wait(1)
#     return tx_hash



def main():
    getWETH(100*10**18)
    # approve_ERC20()
    # swap()
