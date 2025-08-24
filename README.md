# 规则解释：
---

- 模板中的符号：
 -以下是个节点的组合
   - `[]🚀 节点选择（手动选择节点，通常搭配：`[]♻️ 自动选择`.*`[]DIRECT）
   - `[]♻️ 美国节点（所有美国节点）
   - `[]♻️ 自建节点（所有自建节点）
   - `.*（展开所有节点）
   - 其中 `.* 是指所有节点，可以与各节点组合搭配，例如：`[]🚀 节点选择`.* （手动选择所有节点），`[]♻️ 美国节点`.*（自动选择所有美国节点）
   - REJECT=🛑 全球拦截（表示拒绝访问该网站）
   - DIRECT=🎯 全球直连（表示国内直连该网站）
   - 🍃 应用净化（是指APP的广告拦截）

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

