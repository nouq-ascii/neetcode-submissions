class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#"
            encoded_string += word
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []
        leng = ""
        while i < len(s):
            if s[i] == "#":
                b = i
                i += 1
                word = ""
                leng = int(leng)
                while i <= b + leng:
                    word += s[i]
                    i += 1
                decoded_list.append(word)
                leng = ""
            else:
                leng += s[i]
                i += 1
        return decoded_list