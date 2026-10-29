# selenium
selenium Browser 

## 无头浏览器登录脚本【以Lunes为例：含Cloudflare验证】
> 需要设置的变量
> 
> Settings-->Secrets and variables--->actions--->
- Secrets
  - PASSWORD  [**必填**：设置账号的密码]
- Variables
  - ACCOUNTS  [**必填**：账号清单，逗号`,`间隔]
  - HY2_URL   [可选：Hysteria2代理连接]
  - TG_API    [可选：tg自定义接口]

> 使用Variables方便后期查看相关信息；便于修改。

> `HY2_URL` :正常使用hysteria2节点链接
```
hyteria2://UUID@IP:PORT?sni=www.bing.com
```
```
浏览器导航操作
self.open(url) - 导航到指定URL
self.go_back() - 返回上一页
self.get_current_url() - 获取当前页面URL
self.get_title() - 获取当前页面标题
self.get_page_source() - 获取当前页面HTML源代码

元素交互操作
self.type(selector, text) - 在指定元素输入文本
self.click(selector) - 点击指定元素
self.click_link(link_text) - 点击包含指定文本的链接
self.select_option_by_text(dropdown_selector, option) - 在下拉菜单中选择指定文本的选项
self.hover_and_click(hover_selector, click_selector) - 先悬停在指定元素上，再点击另一个元素
self.drag_and_drop(drag_selector, drop_selector) - 执行拖放操作

元素状态检查
self.get_text(selector) - 获取元素文本内容
self.get_attribute(selector, attribute) - 获取元素属性值
self.is_element_visible(selector) - 检查元素是否可见
self.is_text_visible(text, selector) - 检查文本在元素中是否可见

窗口和框架操作
self.switch_to_frame(frame) - 切换到iframe
self.switch_to_default_content() - 从iframe切换回主文档
self.open_new_window() - 打开新窗口
self.switch_to_window(window) - 切换到指定窗口
self.switch_to_default_window() - 切换回默认窗口

驱动和会话管理
self.get_new_driver(OPTIONS) - 使用指定选项创建新驱动
self.switch_to_driver(driver) - 切换到指定驱动
self.switch_to_default_driver() - 切换回默认驱动

等待和断言
self.wait_for_element(selector) - 等待元素可见
self.sleep(seconds) - 强制等待指定秒数
self.assert_element(selector) - 断言元素可见
self.assert_text(text, selector) - 断言元素包含指定文本
self.assert_exact_text(text, selector) - 断言元素文本与指定文本完全一致
self.assert_title(title) - 断言页面标题
self.assert_downloaded_file(file) - 断言文件已下载
self.assert_no_404_errors() - 断言没有404错误
self.assert_no_js_errors() - 断言没有JavaScript错误
```
其他操作
self.save_screenshot(name) - 保存当前页面截图
