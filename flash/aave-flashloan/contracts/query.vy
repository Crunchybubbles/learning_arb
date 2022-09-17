# @version 0.3.2

interface IUniswapV2Pair:
          def token0() -> address: view
          def token1() -> address: view
          def getReserves() -> (uint256, uint256, uint256): view

interface IUniswapV2Factory:
          def allPairs(index: uint256) -> address: view


struct Pool:
       pool_address: address
       token0: address
       token1: address
       reserve0: uint256
       reserve1: uint256
@view
@external
def getPairsData(factory: address, start: uint256) -> Pool[50000]:
    pools: Pool[50000] = empty(Pool[50000])
    
    for i in range(start, start+50000):
       pool_addr: address = IUniswapV2Factory(factory).allPairs(i) 


       reserves_0: uint256 = 0
       reserves_1: uint256 = 0
       time: uint256 = 0
       (reserves_0, reserves_1, time) = IUniswapV2Pair(pool_addr).getReserves()
       
       pool: Pool = Pool({
       pool_address: pool_addr,
       token0: IUniswapV2Pair(pool_addr).token0(),
       token1: IUniswapV2Pair(pool_addr).token1(),
       reserve0: reserves_0,
       reserve1: reserves_1
       })
       pools[i] = pool
    return pools          
