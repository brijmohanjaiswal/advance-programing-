def brijknap(weights, values, capacity):
  n = len(weights)
  dp = [[0] * (capacity + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
      for w in range(capacity + 1):
          if weights[i - 1] <= w:
              dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
          else:
              dp[i][w] = dp[i - 1][w]

  return dp[n][capacity]



max_value = brijknap([2,3,45], [4,5,6], 5)
print(f"Maximum value that can be obtained: {max_value}")
