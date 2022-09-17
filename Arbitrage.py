# import numpy as np

# import brownie
# from brownie import accounts
from web3 import Web3
import os
import time
import json

# from uniswapqueryabi.py import *
# w3 = Web3(Web3.HTTPProvider("https://localhost:8545"))
w3 = Web3(
    Web3.HTTPProvider("http://localhost:8545")
)


UNISWAP_LOOKUP_CONTRACT_ADDRESS = "0x5EF1009b9FCD4fec3094a5564047e190D72Bd511"

UNISWAP_V3_FACTORY_ADDRESS = "0x1F98431c8aD98523631AE4a59f267346ea31F984"
UNISWAP_FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
SUSHISWAP_FACTORY_ADDRESS = "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac"
FACTORY_ADDRESSES = [UNISWAP_FACTORY_ADDRESS, SUSHISWAP_FACTORY_ADDRESS]

UNISWAP_V2_ROUTER_02 = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

AAVE_V2_LENDING_POOL = "0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9"

BLACKLIST_TOKENS = [
    "0x02ba7b2026D26896bc1368e6bEf4349d2f595B68",
    "0x566113069683Ce664958A784f18336B4020a1350",
    "0xa16001DD47f505B7B7c5639c710A52209E4e8904",
    "0x8707dEDB55f4AB2d17Ae849061bF034334d1c8a0",
    "0x86FADb80d8D2cff3C3680819E4da99C10232Ba0F",
    "0x4D13d624a87baa278733c068A174412AfA9ca6C8",
    "0x905D3237dC71F7D8f604778e8b78f0c3ccFF9377",
    "0xDADA00A9C23390112D08a1377cc59f7d03D9df55",
    "0x0Ba45A8b5d5575935B8158a88C631E9F9C95a2e5",
]

WETH_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"  # 18 decimals
DAI_ADDRESS = "0x6B175474E89094C44Da98b954EedeAC495271d0F"  # 18 decimals
YFI_ADDRESS = "0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e"  # 18 decimals
WBTC_ADDRESS = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"  # 8 decimals
USDT_ADDRESS = "0xdAC17F958D2ee523a2206206994597C13D831ec7"  # 6 decimals
ZRX_ADDRESS = "0xE41d2489571d322189246DaFA5ebDe1F4699F498"  # 18 decimals
UNI_ADDRESS = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"  # 18 decimals
AAVE_ADDRESS = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"  # 18 decimals
BAT_ADDRESS = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"  # 18 decimals
BUSD_ADDRESS = "0x4Fabb145d64652a948d72533023f6E7A623C7C53"  # 18 decimals
ENJ_ADDRESS = "0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c"  # 18 decimals
KNC_ADDRESS = "0xdd974D5C2e2928deA5F71b9825b8b646686BD200"  # 18 decimals
LINK_ADDRESS = "0x514910771AF9Ca656af840dff83E8264EcF986CA"  # 18 decimals
MANA_ADDRESS = "0x0F5D2fB29fb7d3CFeE444a200298f468908cC942"  # 18 decimals
MKR_ADDRESS = "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2"  # 18 decimals
REN_ADDRESS = "0x408e41876cCCDC0F92210600ef50372656052a38"  # 18 decimals
SNX_ADDRESS = "0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F"  # 18 decimals
sUSD_ADDRESS = "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51"  # 18 decimals
TUSD_ADDRESS = "0x0000000000085d4780B73119b644AE5ecd22b376"  # 18 decimals
USDC_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"  # 6 decimals
CRV_ADDRESS = "0xD533a949740bb3306d119CC777fa900bA034cd52"  # 18 decimals
GUSD_ADDRESS = "0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd"  # 2 decimals
BAL_ADDRESS = "0xba100000625a3754423978a60c9317c58a424e3D"  # 18 decimals
xSUSHI_ADDRESS = "0x8798249c2E607446EfB7Ad49eC89dD1865Ff4272"  # 18 decimals
renFIL_ADDRESS = "0xD5147bc8e386d91Cc5DBE72099DAC6C9b99276F5"  # 18 decimals
RAI_ADDRESS = "0x03ab458634910AaD20eF5f1C8ee96F1D6ac54919"  # 18 decimals

flashabletokens = [
    WETH_ADDRESS,
    DAI_ADDRESS,
    YFI_ADDRESS,
    WBTC_ADDRESS,
    USDT_ADDRESS,
    ZRX_ADDRESS,
    UNI_ADDRESS,
    AAVE_ADDRESS,
    BAT_ADDRESS,
    BUSD_ADDRESS,
    ENJ_ADDRESS,
    KNC_ADDRESS,
    LINK_ADDRESS,
    MANA_ADDRESS,
    MKR_ADDRESS,
    REN_ADDRESS,
    SNX_ADDRESS,
    sUSD_ADDRESS,
    TUSD_ADDRESS,
    USDC_ADDRESS,
    CRV_ADDRESS,
    GUSD_ADDRESS,
    BAL_ADDRESS,
    xSUSHI_ADDRESS,
    renFIL_ADDRESS,
    RAI_ADDRESS,
]
flashable_tokens_dict = {
    WETH_ADDRESS: "WETH_ADDRESS",
    DAI_ADDRESS: "DAI_ADDRESS",
    YFI_ADDRESS: "YFI_ADDRESS",
    WBTC_ADDRESS: "WBTC_ADDRESS",
    USDT_ADDRESS: "USDT_ADDRESS",
    ZRX_ADDRESS: "ZRX_ADDRESS",
    UNI_ADDRESS: "UNI_ADDRESS",
    AAVE_ADDRESS: "AAVE_ADDRESS",
    BAT_ADDRESS: "BAT_ADDRESS",
    ENJ_ADDRESS: "ENJ_ADDRESS",
    KNC_ADDRESS: "KNC_ADDRESS",
    LINK_ADDRESS: "LINK_ADDRESS",
    MANA_ADDRESS: "MANA_ADDRESS",
    MKR_ADDRESS: "MKR_ADDRESS",
    REN_ADDRESS: "REN_ADDRESS",
    SNX_ADDRESS: "SNX_ADDRESS",
    sUSD_ADDRESS: "sUSD_ADDRESS",
    TUSD_ADDRESS: "TUSD_ADDRESS",
    USDC_ADDRESS: "USDC_ADDRESS",
    CRV_ADDRESS: "CRV_ADDRESS",
    GUSD_ADDRESS: "GUSD_ADDRESS",
    BAL_ADDRESS: "BAL_ADDRESS",
    xSUSHI_ADDRESS: "xSUSHI_ADDRESS",
    renFIL_ADDRESS: "renFIL_ADDRESS",
    RAI_ADDRESS: "RAI_ADDRESS",
    BUSD_ADDRESS: "BUSD_ADDRESS",
}
# print(flashable_tokens_dict)


def fixunits(token_address):
    if token_address == USDT_ADDRESS or token_address == USDC_ADDRESS:
        return 10 ** 6
    if token_address == WBTC_ADDRESS:
        return 10 ** 8
    if token_address == GUSD_ADDRESS:
        return 10 ** 2
    else:
        return 10 ** 18


# def get_account(id):
#     return accounts.load(id)

# def approve_erc20(amount, to, erc20_address, account):
#     print("Approving ERC20...")
#     erc20 = interface.IERC20(erc20_address)
#     tx_hash = erc20.approve(to, amount, {"from": account})
#     print("Approved!")
#     tx_hash.wait(1)
#     return tx_hash


with open("uniswapqueryabi.json") as f:
    uniswapqueryabi = json.load(f)
with open("aaveflashable.json") as f:
    aaveflashableabi = json.load(f)
with open("uniswapV2router02.json") as f:
    uniswapV2router02abi = json.load(f)
uniswapQuery = w3.eth.contract(
    address=UNISWAP_LOOKUP_CONTRACT_ADDRESS, abi=uniswapqueryabi
)
aaveflashable = w3.eth.contract(address=AAVE_V2_LENDING_POOL, abi=aaveflashableabi)
uniswapV2router02 = w3.eth.contract(
    address=UNISWAP_V2_ROUTER_02, abi=uniswapV2router02abi
)

# flashabletokens = aaveflashable.functions.getReservesList().call()
# print(flashabletokens)

# def executeswap(amountIn,minamountOut, tokenpath, goesTo , router_address):
#     expiration_block = w3.eth.get_block_number() + 2
#     swap_tx = uniswapV2router02.functions.swapTokensForExactTokens(amountIn, minamountOut, tokenpath, account.address, {"from": account} ).transact()
#     swap_tx.wait(1)
#     return swap_tx

# print(w3.eth.get_block_number())


start = [0, 1001, 2001]
stop = [1000, 2000, 3000]

# marketdata = {}
# adressbook = []
# for facaddr in FACTORY_ADDRESSES:
#     data = uniswapQuery.functions.getPairsByIndexRange(facaddr,start,stop).call()
#     for i in range(len(data)):
#         pair = data[i]
#         marketAddress = pair[2]
#         marketdata[marketAddress] = [pair[0],pair[1]]
#         adressbook += [marketAddress]
#         for k in BLACKLIST_TOKENS:
#             if k == pair[0]  or k == pair[1]:
#                 # print('found bad tokens')
#                 try:
#                     del marketdata[marketAddress]
#                     adressbook.remove(marketAddress)
#                     print(f'bad token removed {pair}')
#                 except KeyError:
#                     pass


marketdata = {}
adressbook = []
for k in [0, 1]:
    for facaddr in FACTORY_ADDRESSES:
        print(start[k], stop[k])
        data = uniswapQuery.functions.getPairsByIndexRange(
            facaddr, start[k], stop[k]
        ).call()
        for i in range(len(data)):
            pair = data[i]
            if pair[0] in BLACKLIST_TOKENS:
                print(f"bad token found {pair}")
            elif pair[1] in BLACKLIST_TOKENS:
                print(f"bad token found {pair}")
            else:
                marketAddress = pair[2]
                marketdata[marketAddress] = [pair[0], pair[1]]
                adressbook += [marketAddress]
# print(marketdata)
# print(adressbook)


def marketdictwithreserves(pairlist):
    reserves = uniswapQuery.functions.getReservesByPairs(pairlist).call()
    reservemarketdict = {}
    for k, i in enumerate(pairlist):
        reservemarketdict[i] = {
            marketdata[i][0]: reserves[k][0],
            marketdata[i][1]: reserves[k][1],
        }
    return reservemarketdict


pooldepth = marketdictwithreserves(adressbook)

print(len(pooldepth))

# # emptypoolcount = 0
# for pool in marketdictwithreserves(adressbook):
#     if pooldepth[pool][marketdata[pool][0]] <= .002*fixunits(marketdata[pool][0]) or pooldepth[pool][marketdata[pool][1]] <=.002*fixunits(marketdata[pool][1]):
#         # emptypoolcount += 1
#         del pooldepth[pool]
#         del marketdata[pool]
#         adressbook.remove(pool)
#         # print(f'removed pool: {pool}')

for pool in marketdictwithreserves(adressbook):
    if (
        marketdata[pool][0] == USDT_ADDRESS
        or marketdata[pool][0] == USDC_ADDRESS
        or marketdata[pool][0] == DAI_ADDRESS
        or marketdata[pool][0] == GUSD_ADDRESS
        or marketdata[pool][0] == BUSD_ADDRESS
        or marketdata[pool][0] == sUSD_ADDRESS
        or marketdata[pool][0] == TUSD_ADDRESS
        or marketdata[pool][1] == USDT_ADDRESS
        or marketdata[pool][1] == USDC_ADDRESS
        or marketdata[pool][1] == DAI_ADDRESS
        or marketdata[pool][1] == GUSD_ADDRESS
        or marketdata[pool][1] == BUSD_ADDRESS
        or marketdata[pool][1] == sUSD_ADDRESS
        or marketdata[pool][1] == TUSD_ADDRESS
    ):
        if pooldepth[pool][marketdata[pool][0]] <= 100 * fixunits(
            marketdata[pool][0]
        ) or pooldepth[pool][marketdata[pool][1]] <= 100 * fixunits(
            marketdata[pool][1]
        ):
            del pooldepth[pool]
            del marketdata[pool]
            adressbook.remove(pool)
    else:
        if pooldepth[pool][marketdata[pool][0]] <= 0.002 * fixunits(
            marketdata[pool][0]
        ) or pooldepth[pool][marketdata[pool][1]] <= 0.002 * fixunits(
            marketdata[pool][1]
        ):
            del pooldepth[pool]
            del marketdata[pool]
            adressbook.remove(pool)
        # emptypoolcount += 1
print(len(pooldepth))
beginning = time.time()
# print('pooldepth')
# for market in marketdata:
#     print(marketdata[market])
# print(pooldepth)
# for i in marketdata():
#     if i and j in
# if i in

# print(marketdata)


def swap(amount, reserveA, reserveB, marketAddress, tokenIN):
    tokenin = tokenIN
    tokenA = marketdata[marketAddress][0]
    tokenB = marketdata[marketAddress][1]
    amountINwithFEE = 997 * amount
    # k = reserveA*reserveB
    if tokenin == tokenA:
        amountout = reserveB * amountINwithFEE / (reserveA * 1000 + amountINwithFEE)
        return amountout, tokenB
    if tokenin == tokenB:
        amountout = reserveA * amountINwithFEE / (reserveB * 1000 + amountINwithFEE)
        return amountout, tokenA


def pricecalc(mkrtaddr, tokenA, tokenB):
    priceA = pooldepth[mkrtaddr][tokenB] / pooldepth[mkrtaddr][tokenA]
    priceB = pooldepth[mkrtaddr][tokenA] / pooldepth[mkrtaddr][tokenB]
    pricedtokens = {tokenA: priceA, tokenB: priceB}
    return pricedtokens


# pricedMarkets = {}
# for i,j in enumerate(pooldepth):
#     pricedMarkets[j] = pricecalc(j,validpairs[i,0],validpairs[i,1])


def listofmarketsoftoken(marketlist, token):
    info = []
    for market in marketlist:
        if token == marketlist[market][0] or token == marketlist[market][1]:
            info.append(market)
    return info


def findbestethmarketfortoken(amount, token, marketslist):
    wEthpools = listofmarketsoftoken(marketslist, WETH_ADDRESS)
    validpools = {}
    mostEth = 0
    for pool in wEthpools:
        if marketdata[pool][0] == token or marketdata[pool][1] == token:
            validpools[pool] = swap(
                amount,
                pooldepth[pool][marketdata[pool][0]],
                pooldepth[pool][marketdata[pool][1]],
                pool,
                token,
            )[0]
            if validpools[pool] > mostEth:
                mostEth = validpools[pool]
                bestpool = pool
    return bestpool, mostEth


flashabletokenswithmarketdatadict = {}
for token in flashabletokens:
    flashabletokenswithmarketdatadict[token] = listofmarketsoftoken(marketdata, token)
# print(flashabletokenswithmarketdatadict[flashabletokens[2]])
# print(listofmarketsoftoken(marketdata, '0x0Ba45A8b5d5575935B8158a88C631E9F9C95a2e5'))
# oneERC20token = 1*(1*10**18)

# def oneERC20token(token_address):
#     return
# testamounts = [.01*oneERC20token,oneERC20token, 2*oneERC20token]
testamounts = [0.01, 0.1, 1, 2, 10, 100, 1000, 10000]
testamountsforeachtoken = {}
for i in flashabletokens:
    testamountsforeachtoken[i] = [
        testamounts[0] * fixunits(i),
        testamounts[1] * fixunits(i),
    ]
# print(testamountsforeachtoken)
def findvalue():
    index = 0
    arb = []
    flashloanfee = 9
    for token, initialamounts in testamountsforeachtoken.items():
        print(flashable_tokens_dict[token])
        print(index)
        for initialamount in initialamounts:
            index += 1
            # print(token)
            # print(initialamount)
            for market in flashabletokenswithmarketdatadict[token]:
                index += 1
                newtoken1 = swap(
                    initialamount,
                    pooldepth[market][marketdata[market][0]],
                    pooldepth[market][marketdata[market][1]],
                    market,
                    token,
                )[1]
                newamount1 = swap(
                    initialamount,
                    pooldepth[market][marketdata[market][0]],
                    pooldepth[market][marketdata[market][1]],
                    market,
                    token,
                )[0]
                newmarkets1 = listofmarketsoftoken(marketdata, newtoken1)
                # print(newtoken1, newamount1)
                for market2 in newmarkets1:
                    index += 1
                    newtoken2 = swap(
                        newamount1,
                        pooldepth[market2][marketdata[market2][0]],
                        pooldepth[market2][marketdata[market2][1]],
                        market2,
                        newtoken1,
                    )[1]
                    newamount2 = swap(
                        newamount1,
                        pooldepth[market2][marketdata[market2][0]],
                        pooldepth[market2][marketdata[market2][1]],
                        market2,
                        newtoken1,
                    )[0]
                    # print(newtoken2, newamount2)
                    if newtoken2 == token:
                        profit = (newamount2 - initialamount) - (
                            initialamount * flashloanfee
                        ) / 10000
                        if profit > 0:
                            if token == WETH_ADDRESS:
                                arb.append(
                                    [
                                        token,
                                        initialamount,
                                        profit / 10 ** 18,
                                        newamount2,
                                        [market, market2],
                                        [token, newtoken1, newtoken2],
                                    ]
                                )
                            else:
                                Ethprofit = (
                                    findbestethmarketfortoken(
                                        profit, token, marketdata
                                    )[1]
                                    / 10 ** 18
                                )
                                Ethmarket = findbestethmarketfortoken(
                                    profit, token, marketdata
                                )[0]
                                arb.append(
                                    [
                                        token,
                                        initialamount,
                                        Ethprofit,
                                        Ethprofit,
                                        [market, market2, Ethmarket],
                                        [token, newtoken1, newtoken2, WETH_ADDRESS],
                                    ]
                                )
                            # print(f'profit found {Ethprofit}')
                            # print(arb)
                    else:
                        newmarkets3 = listofmarketsoftoken(marketdata, newtoken2)
                        for market3 in newmarkets3:
                            index += 1
                            newtoken3 = swap(
                                newamount2,
                                pooldepth[market3][marketdata[market3][0]],
                                pooldepth[market3][marketdata[market3][1]],
                                market3,
                                newtoken2,
                            )[1]
                            newamount3 = swap(
                                newamount2,
                                pooldepth[market3][marketdata[market3][0]],
                                pooldepth[market3][marketdata[market3][1]],
                                market3,
                                newtoken2,
                            )[0]
                            if newtoken3 == token:
                                # print(newamount3, initialamount)
                                profit = (newamount3 - initialamount) - (
                                    initialamount * flashloanfee
                                ) / 10000
                                if profit > 0:
                                    if token == WETH_ADDRESS:
                                        arb.append(
                                            [
                                                token,
                                                initialamount,
                                                profit / 10 ** 18,
                                                newamount3,
                                                [market, market2, market3],
                                                [
                                                    token,
                                                    newtoken1,
                                                    newtoken2,
                                                    newtoken3,
                                                ],
                                            ]
                                        )
                                    else:
                                        Ethprofit = (
                                            findbestethmarketfortoken(
                                                profit, token, marketdata
                                            )[1]
                                            / 10 ** 18
                                        )
                                        # Ethmarket = findbestethmarketfortoken(profit, token, marketdata)[0]
                                        arb.append(
                                            [
                                                token,
                                                initialamount,
                                                Ethprofit,
                                                Ethprofit,
                                                [market, market2, market3],
                                                [
                                                    token,
                                                    newtoken1,
                                                    newtoken2,
                                                    newtoken3,
                                                    WETH_ADDRESS,
                                                ],
                                            ]
                                        )
                                # print(f'profit found {Ethprofit}')

                                # print(arb)
                            # else:
                            #     newmarkets4 = listofmarketsoftoken(marketdata,newtoken3)
                            #     for market4 in newmarkets4:
                            #         index += 1
                            #         newtoken4 = swap(newamount3, pooldepth[market4][marketdata[market4][0]],pooldepth[market4][marketdata[market4][1]],market4,newtoken3)[1]
                            #         newamount4 = swap(newamount3, pooldepth[market4][marketdata[market4][0]],pooldepth[market4][marketdata[market4][1]],market4,newtoken3)[0]
                            #         if newtoken4 == token:
                            #             profit = newamount4 - initialamount - (initialamount*flashloanfee)/10000
                            #             if profit > 0:
                            #                 Ethprofit = findbestethmarketfortoken(profit, token, marketdata)[1]
                            #                 Ethmarket = findbestethmarketfortoken(profit, token, marketdata)[0]
                            #                 arb.append([token, initialamount, Ethprofit, Ethmarket , market, market2, market3,market4])
                            # arb.append([token, initialamount, profit, market, market2, market3, market4])
                            # print(arb)
                            #         else:
                            #             newmarkets5 = listofmarketsoftoken(marketdata,newtoken4)
                            #             for market5 in newmarkets5:
                            #                 newtoken5 = swap(newamount4, pooldepth[market5][marketdata[market5][0]], pooldepth[market5][marketdata[market5][1]], market5, newtoken4)[1]
                            #                 newamount5 = swap(newamount4, pooldepth[market5][marketdata[market5][0]], pooldepth[market5][marketdata[market5][1]], market5, newtoken4)[0]
                            #                 if newtoken5 == token:
                            #                     profit = newamount5 - initialamount -initialamount*flashloanfee
                            #                     if profit > 0:
                            #                         Ethprofit = findbestethmarketfortoken(profit, token, marketdata)[1]
                            #                         Ethmarket = findbestethmarketfortoken(profit, token, marketdata)[0]
                            #                         arb.append([token, initialamount, Ethprofit, Ethmarket , market, market2, market3, market4, market5])
    # print(index)
    return arb


# print(findvalue())
# print(arb[0][2:])
# print(arb)


def findbest():
    best = {}
    for i in findvalue():
        # print(i)
        token = i[0]
        amount = i[1]
        profit = i[2]
        amountOut = i[3]
        pools = i[4]
        path = i[5]
        # finalselltoEth = i[3]
        # print(token,profit)
        if token in best.keys():
            if profit > best[token][0]:
                best[token] = [profit, amount, amountOut, pools, path]
        else:
            best[token] = [profit, amount, amountOut, pools, path]
    return best


# print(best)
best = findbest()
# print()
for i in best:
    print(flashable_tokens_dict[i])
    print(
        i,
        f"    Ethprofit {best[i][0]}    initialamount {best[i][1]}   amount out {best[i][2]}   pools {best[i][3]}   market path {best[i][4]}",
    )
    print()
# print(findbest())
end = time.time()
print(end - beginning)

# def minOut(amount_out):
#     return amount_out-((amount_out*2)/100)
#
# def main():
#     account = get_account('testacc')
#     best = findbest()
#     tx = approve_erc20(best[DAI_ADDRESS][1], UNISWAP_V2_ROUTER_02, DAI_ADDRESS, account)
#     tx.wait(1)
#     executeswap(best[DAI_ADDRESS][1],minOut(best[DAI_ADDRESS][2]),best[DAI_ADDRESS][3:], account, UNISWAP_V2_ROUTER_02)

# yfi_market = listofmarketsoftoken(marketdata,WBTC_ADDRESS)
# print(yfi_market)

# print(flashabletokenswithmarketdatadict)
# for i in flashabletokenswithmarketdatadict:
#     print(flashable_tokens_dict[i])
#     print(i)
#     print(flashabletokenswithmarketdatadict[i])
#     tokendepth = 0
#     for j in flashabletokenswithmarketdatadict[i]:
#         tokendepth += pooldepth[j][i]
#     print(tokendepth)
#     print()

# print(pooldepth[j][i])
# print(flashabletokenswithmarketdatadict)

# print(pooldepth)
# test = {}
# test[arb[0][0]] = [arb[0][2],arb[0][3:]]
# print(test[arb[0][0]][0])
# print(newtoken1, newamount1, newmarkets1)

# print(listofmarketsoftoken(marketdata,'0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'))

#
# print(flashabletokens)
# validpairsdict = {}
# for i in validpairs:
#     validpairsdict[i[2]] = [i[0],i[1]]
# def swapcalc(marketwithreservesA,marketwithreservesB):

# for i in validpairs:
#     print(f'amount of {i[1]} from market {i[2]}')
#     print(swap(10,i[0],i[1],validpairs,i[2],i[0]))

# print(i)

# marketpair = {}


# print(validpairs)

# class Market:
#
#     def __init__(self,tokenA,tokenB,pooladdress):
#         self.tokenA = tokenA
#         self.tokenB = tokenB
#         self.pooladdress = pooladdress

# def updatereserves(self,pooladdress):
#     return uniswapQuery.functions.getReservesByPairs(pooladdress).call()

# test = Market(validpairs[0][0],validpairs[0][1],validpairs[0][2])

# print(test.tokenB)
# print(test.pooladdress)
# print(test)
# for i in range(len(validpairs)):
#     test = Market(validpairs[i][0],validpairs[i][1],validpairs[i][2])


# print(test.tokenA)
# print(test.pooladdress)
# print(validpairs)
# print(len(validpairs))


# print(swap((100),validpairs[0][0],validpairs[0][1],validpairs,validpairs[0][2],validpairs[0][1]))
# print('with reserves')
# print(marketdictwithreserves(validpairs))
# print('validpairs')
# print(validpairs)


# def removeEmptypools(marketaddresses):
#     entrystodelete = []
#     for market in marketaddresses:
#         for tokens in marketaddresses[market]:
#             if marketaddresses[market][tokens] == 0:
#                 entrystodelete.append(market)
#     return entrystodelete
#
# emptypools = removeEmptypools(pooldepth)
# emptiestpools = []
# for i in emptypools:
#     if i not in emptiestpools:
#         emptiestpools.append(i)
#
# for i in range(len(emptiestpools)):
#     del pooldepth[emptiestpools[i]]


# print(pricedMarkets)


# print(j)
# print(pricedMarkets[j])
# print(sorted(pricedMarkets))
# addr = []
# for i in pricedMarkets:
#     for j in pricedMarkets[i]:
#         addr += [(j,pricedMarkets[i][j])]
# print(flashabletokens)

#


#
# for e in flashabletokenswithmarketdatadict:
#     print(e)
#     print(flashabletokenswithmarketdatadict[e])

# print(pricedMarkets['0x06da0fd433C1A5d7a4faa01111c044910A184553'])

# for i in validpairs:
#     print(i)
# print(validpairs)
# tokenmarketdict = {}
# for token in flashabletokens:
#     tokenmarketdict[token] = [listofmarketsoftoken(token)]

# print(sorted(pricedMarkets.values()))

# for i in sorted(addr):
#     print(i)


# for m, n in pooldepth[validpairs[0][2]].items():
#     print(m, n)
# print(pooldepth[validpairs[0][2]])
# print(pricecalc(validpairs[0][2],validpairs[0][0],validpairs[0][1]), validpairs[0][2])
# print(pooldepth)

# for i in pooldepth:
#     print(i)
# for i in range(len(validpairs)):
#     print(marketdictwithreserves(validpairs)[validpairs[i][2]])
# for j in range(len(validpairs)):
#     print(j)
#     for i in (0,1):
#         print(pooldepth[validpairs[j][2]][validpairs[j][i]])
# marketsbytokens(validpairs)
# print(marketsbytokens(validpairs))
# print(marketsbytokens(validpairs)['tokens'])
# print(marketdictwithreserves(validpairs))


# def swap( amountA, amountB ,marketlist):
#     for i in marketlist:
#         tokens = marketlist[i]
#         for n in tokens:
#             print(n)
#         # print(tokens)
#     # tokenB =
#         pooladdr = i

# swap(1,1,marketdictwithreserves(validpairs))


# print(marketdictwithreserves(validpairs))

# print(onlyadress(validpairs)[0])
# print(pricedmarkets)
# print(reserves)
# print(validpairs)


# print(validpairs[0][2])

# print(flashabletokens)

# print(validpairs)


# uniswapQuery = w3.eth.contract(address = UNISWAP_LOOKUP_CONTRACT_ADDRESS, abi = uniswapqueryabi )
# data = uniswapQuery.functions.getPairsByIndexRange(UNISWAP_FACTORY_ADDRESS,0,1).call()
# print(data[0][0]) #token a
# print(data[0][1]) #token b
# print(data[0][2]) #market address


# newblock = w3.eth.filter('latest')
# logs = w3.eth.get_logs('latest', 'blockNumber')

# while True:
#     block = w3.eth.get_block('latest')
#     print(block.number)
#     time.sleep(2)
# print(UNISWAP_LOOKUP_CONTRACT_ADDRESS)
