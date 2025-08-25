# Clash 配置模板说明：
---

> ⭐ **一、节点组：（只是名称，不包含任何节点）

custom_proxy_group=🚀 节点选择
custom_proxy_group=♻️ 自动选择

自建节点组（可自定义）

custom_proxy_group=♻️ 美国节点
custom_proxy_group=♻️ 自建节点
custom_proxy_group=🚀 美国选择
custom_proxy_group=🚀 美日选择

2.节点组后面只能2种选择：

select（手动选择）
url-test（自动选择）

3.各国节点集合：

包含美国节点集合：(United States)
包含日本节点集合：(Japan)
包含所有节点集合：.*

注：它们之间的隔离号：`

---

> ⭐ **二、创建各“节点组”

- 举例1：“🚀 节点选择”节点组

custom_proxy_group=🚀 节点选择`select`[]♻️ 自动选择`.*`[]DIRECT

解释：手动选择3种类型：[]♻️ 自动选择 +  .*（所有节点） +  []DIRECT（直连）


- 举例2：“♻️ 自动选择”节点组

custom_proxy_group=♻️ 自动选择`url-test`.*`http://www.gstatic.com/generate_204`300,,50

解释：自动选择所有节点，因为包含：url-test（自动选择）和 .*`（所有节点）


- 举例3：创建“🚀 美国选择”节点组，可手动选择美国节点

custom_proxy_group=🚀 美国选择`select`(United States)`[]♻️ 美国节点

解释：手动选择2种类型：(United States) （美国节点集合） +  []♻️ 美国节点（美国自动选择集合）


- 举例4：创建“🚀 美日选择”节点组，手动选择美国日本节点

custom_proxy_group=🚀 美日选择`select`(United States)`(Japan)`[]♻️ 美日自动

解释：手动选择2种类型：美日节点集合 + ♻️ 美日自动


- 举例5：创建“♻️ 美日自动”节点组，自动选择美国日本节点的集合

custom_proxy_group=♻️ 美日自动`url-test`(United States)`(Japan)`http://www.gstatic.com/generate_204`300,,50

解释：自动选择美国日本节点，包含：url-test、(United States)`(Japan)


> ⭐ **三、各分流规则使用“节点组”分流

需要在“节点组”名称前加符合“[]”，例如：🚀 美国选择，改为：`[]🚀 美国选择

举例：🎥 GoogleUI 分流规则

custom_proxy_group=🎥 GoogleUI`select`[]🚀 美国选择`[]♻️ 自建节点

解释：“🎥 GoogleUI”分流规则可选择2种节点集合：🚀 美国选择  +  ♻️ 自建节点
      后面不需要再添加：[]♻️ 美国节点 + .*


其他符号说明：
🛑 全球拦截=REJECT（拒绝）
🎯 全球直连=DIRECT（直连）
🍃 应用净化（APP的广告拦截，没有使用）
PROXY（代理）

---

# Clash 规则匹配类型如下：
---

- DOMAIN-SUFFIX：匹配域名后缀，例如：DOMAIN-SUFFIX,google.com：匹配 google.com和 www.google.com
- DOMAIN：完全匹配域名
- DOMAIN-KEYWORD：关键词匹配域名
- IP-CIDR / IP-CIDR6：IP段匹配，IP CIDR 范围，可以添加 no-resolve 避免触发 DNS 解析。
- SRC-IP-CIDR：源IP段匹配
- GEOIP：GEOIP数据库（国家代码）匹配
- DST-PORT：目标端口匹配
- SRC-PORT：源端口匹配
- MATCH：全匹配（一般放在最后）

---


