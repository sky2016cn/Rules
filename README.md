# Clash 规则匹配类型如下：

- DOMAIN-SUFFIX：匹配域名后缀，例如 DOMAIN-SUFFIX,google.com 匹配 google.com 和 www.google.com。
- DOMAIN：完全匹配域名
- DOMAIN-KEYWORD：关键词匹配域名
- IP-CIDR / IP-CIDR6：IP段匹配，IP CIDR 范围，可以添加 no-resolve 避免触发 DNS 解析。
- SRC-IP-CIDR：源IP段匹配
- GEOIP：GEOIP数据库（国家代码）匹配
- DST-PORT：目标端口匹配
- SRC-PORT：源端口匹配
- MATCH：全匹配（一般放在最后）

