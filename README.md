# luci-app-CampusNetCU #

适用于 UJN 等院校的联通校园网自动验证插件

本项目仅提供了x86架构的ipk包，其他平台可按照以下流程自行编译

## LEDE 或 OpenWrt 编译 ##

克隆本项目至 lede 或 openwrt 的 `feeds/luci/applications/`

```shell
cd feeds/luci/applications/

git clone https://github.com/nicholas9698/luci-app-campusnet.git
```

返回 lede 或 openwrt 根目录，然后使用以下命令编译本插件

```shell
cd lede

./scripts/feeds update -a

./scripts/feeds install -a

make package/feeds/luci/luci-app-campusnet/compile V=s
```

编译的 ipk 包将在 `bin/packages/target/luci/` 中生成