import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        #IPv4
        ipv4Chunk = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        ipv4Pattern = re.compile(r'^(' + ipv4Chunk + r'\.){3}' + ipv4Chunk + r'$')      
        #similarly for IPv6
        ipv6Chunk = r'([0-9a-fA-F]{1,4})'
        ipv6Pattern = re.compile( r'^(' + ipv6Chunk + r'\:){7}' + ipv6Chunk + r'$')
        
        if ipv4Pattern.match(queryIP): return "IPv4"
        elif ipv6Pattern.match(queryIP): return "IPv6"
        return "Neither"