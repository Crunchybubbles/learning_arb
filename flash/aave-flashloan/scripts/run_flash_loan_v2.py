from brownie import FlashloanV2, accounts, config, network, interface
from brownie.convert import to_bytes
MINIMUM_FLASHLOAN_WETH_BALANCE = 500000000000000000
ETHERSCAN_TX_URL = "https://kovan.etherscan.io/tx/{}"
#params = to_bytes(["0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "0x514910771AF9Ca656af840dff83E8264EcF986CA", "0x3A9FfF453d50D4Ac52A6890647b823379ba36B9E", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"])
param1 = to_bytes("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
param2 = to_bytes("0x514910771AF9Ca656af840dff83E8264EcF986CA")
param3 = to_bytes("0x3A9FfF453d50D4Ac52A6890647b823379ba36B9E")
params = [param1, param2, param3]
#params =""
def main():
    """
    Executes the funcitonality of the flash loan.
    """
    acct = accounts[0]
    print("Getting Flashloan contract...")
    flashloan = FlashloanV2[len(FlashloanV2) - 1]
    weth = interface.WethInterface(config["networks"][network.show_active()]["weth"])
    # We need to fund it if it doesn't have any token to fund!
    if weth.balanceOf(flashloan) < MINIMUM_FLASHLOAN_WETH_BALANCE:
        print("Funding Flashloan contract with WETH...")
        weth.transfer(flashloan, "1 ether", {"from": acct})
    print("Executing Flashloan...")
    tx = flashloan.flashloan(weth, params, {"from": acct})
    print("You did it! View your tx here: " + ETHERSCAN_TX_URL.format(tx.txid))
    return flashloan
