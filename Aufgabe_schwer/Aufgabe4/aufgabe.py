def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[-1]

if __name__ == "__main__":
    m = int(input())
    word_dict = set(input().split())
    s = input()
    print(word_break(s, word_dict))