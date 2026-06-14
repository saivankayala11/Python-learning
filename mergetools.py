def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0,n,k):
        chunk = string[i:i + k]
        seen = ''
        for char in chunk:
            if char not in seen:
                seen += char
        print(seen)                
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)