# 规则解释：
---

- 模板中的符号：
 -以下是各节点组合  
   - `[]🚀 节点选择（手动选择节点，本身不包含节点，必须搭配下方任意节点组合）
   - `[]♻️ 美国节点（所有美国节点）
   - `[]♻️ 自建节点（所有自建节点）
   - `.*（包含所有节点）
   - 🛑 全球拦截=REJECT（拒绝访问）
   - 🎯 全球直连=DIRECT（国内直连）
   - 🍃 应用净化（是指APP的广告拦截）
   - PROXY（表示走代理）

---

# Clash 规则匹配类型如下：

- DOMAIN-SUFFIX：匹配域名后缀，例如：DOMAIN-SUFFIX,google.com：匹配“google.com”和“www.google.com”
- DOMAIN：完全匹配域名
- DOMAIN-KEYWORD：关键词匹配域名
- IP-CIDR / IP-CIDR6：IP段匹配，IP CIDR 范围，可以添加 no-resolve 避免触发 DNS 解析。
- SRC-IP-CIDR：源IP段匹配
- GEOIP：GEOIP数据库（国家代码）匹配
- DST-PORT：目标端口匹配
- SRC-PORT：源端口匹配
- MATCH：全匹配（一般放在最后）

