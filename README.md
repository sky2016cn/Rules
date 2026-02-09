# 规则符合解释：
---

- 模板中的符号：以下是各节点组合  
   - []🚀 节点选择
   - []♻️ 美国节点
   - []♻️ 自建节点
   - 手动选择：select
   - 自动选择：url-test
   - 美国节点集合：(United States)
   - 日本节点集合：(Japan)
   - 所有节点集合：.* 
   - 🛑 全球拦截=REJECT（拒绝）
   - 🎯 全球直连=DIRECT（直连）
   - 🍃 应用净化（APP的广告拦截）
   - PROXY（代理）
   - 注：它们之间有分隔号：`

---

# Clash 规则匹配类型如下：
---

- DOMAIN-SUFFIX：匹配域名后缀，例如：DOMAIN-SUFFIX,google.com：匹配 google.com和 www.google.com
- DOMAIN：完全匹配域名
- DOMAIN-KEYWORD：关键词匹配域名
- IP-CIDR / IP-CIDR6：IP段匹配，IP CIDR 范围，都添加 no-resolve，是为了避免触发 DNS 解析
- SRC-IP-CIDR：源IP段匹配
- GEOIP：GEOIP数据库（国家代码）匹配
- DST-PORT：目标端口匹配
- SRC-PORT：源端口匹配
- MATCH：全匹配（一般放在最后）

---

# IPTV_EPG 文件夹内是脚本自动生成 e1.xml 节目表：
---

- 此为宽带 IPTV 的节目表，来自 EPG 节目表网站：https://epg.51zmt.top:8001/，每2天早上6点自动生成

---
