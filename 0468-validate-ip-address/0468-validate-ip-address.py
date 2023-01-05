import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        #IPv4
        ipv4Chunk = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        ipv4Pattern = re.compile(r'^(' + ipv4Chunk + r'\.){3}' + ipv4Chunk + r'$') 
        #^ is starts with
        #$ is ends with
        #each elements denotes one character only
        #{n} is previous pattern n times
        #r is raw string
        
        #similarly for IPv6
        """
        ipv6Chunk = r'([0-9a-fA-F]{1,4})'
        ipv6Pattern = re.compile( r'^(' + ipv6Chunk + r'\:){7}' + ipv6Chunk + r'$')
        
        if ipv4Pattern.match(queryIP): return "IPv4"
        elif ipv6Pattern.match(queryIP): return "IPv6"
        return "Neither"
        """
        if len(queryIP.split('.'))==4:
            #ipv4Case
            splits = queryIP.split('.')
            dec_digits = set('0123456789')
            for split in splits:
                if len(split)==0 or len(split)>3: return "Neither"
                for char in split:
                    if char not in dec_digits: return "Neither"
                if not (0<=int(split)<=255) or str(int(split))!=split:
                    return "Neither"
            return "IPv4"
        elif len(queryIP.split(':'))==8:
            splits = queryIP.split(':')
            hex_digits = set("0123456789abcdefABCDEF")
            for split in splits:
                if len(split)==0 or len(split)>4: return "Neither"
                for char in split:
                    if char not in hex_digits: return "Neither"
            return "IPv6"
        return "Neither"