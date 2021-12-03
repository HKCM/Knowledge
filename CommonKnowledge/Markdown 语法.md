<iframe id="_atssh935" title="AddThis utility frame" src="https://s7.addthis.com/static/sh.f48a1a04fe8dbf021b4cda1d.html#rand=0.0572621868114811&amp;iit=1635726799354&amp;tmr=load%3D1635726799320%26core%3D1635726799347%26main%3D1635726799350%26ifr%3D1635726799356&amp;cb=0&amp;cdn=0&amp;md=0&amp;kw=&amp;ab=-&amp;dh=support.typora.io&amp;dr=https%3A%2F%2Fcn.bing.com%2F&amp;du=https%3A%2F%2Fsupport.typora.io%2FMarkdown-Reference%2F&amp;href=https%3A%2F%2Fsupport.typora.io%2FMarkdown-Reference%2F&amp;dt=Markdown%20Reference&amp;dbg=0&amp;cap=tc%3D0%26ab%3D0&amp;inst=1&amp;jsl=0&amp;prod=undefined&amp;lng=zh&amp;ogt=image%2Cdescription%2Ctitle%2Curl&amp;pc=men&amp;pub=ra-5ed23a5bcf8c017f&amp;ssl=1&amp;sid=617f35cf832fdfa7&amp;srf=0.01&amp;ver=300&amp;xck=0&amp;xtr=0&amp;og=url%3D%252FMarkdown-Reference%252F%26title%3DMarkdown%2520Reference%26description%3DOverview%2520Markdown%2520is%2520created%2520by%2520Daring%2520Fireball%253B%2520the%2520original%2520guideline%2520is%2520here.%2520Its%2520syntax%252C%2520however%252C%2520varies%2520between%2520different%2520parsers%2520or%2520editors.%2520Typora%2520try%2520to%2520follow%2520GitHub%2520Flavored%2520Markdown%252C%2520but%2520may%2520still%2520have%2520small%2520incompatibilities.%2520Table%2520of%2520Contents%2520Overview%2520Block%2520Elements%2520Paragraph%2520and%2520line%2520breaks%2520Headers%2520Blockquotes%2520Lists%2520Task%2520List%2520(Fenced)%2520Code%2520Blocks%2520Math%2520Blocks%2520Tables%2520Footnotes%2520Horizontal%2520Rules%2520YAML%2520Front%2520Matter%2520Table%2520of%2520Contents%2520(TOC)%2520Span%2520Elements%2520Links%2520Inline%2520Links%2520Internal%2520Links%2520Reference%2520Links%2520URLs%2520Images%2520Emphasis%2520Strong%2520Code%2520Strikethrough%2520Emoji%2520%253Ahappy%253A%2520Inline%2520Math%2520Subscript%2520Superscript%2520Highlight%2520HTML%2520Underlines%2520Embed%2520Contents%2520Video%2520Other%2520HTML%2520Support%2520Block%2520Elements%2520Paragraph%2520and%2520line...%26image%3Dhttp%253A%252F%252Ftypora.io%252Fimg%252Ftwitter-sum.png&amp;csi=undefined&amp;rev=v8.28.8-wp&amp;ct=1&amp;xld=1&amp;xd=1" style="height: 1px; width: 1px; position: absolute; top: 0px; z-index: 100000; border: 0px; left: 0px;"></iframe>

# Markdown 语法



[toc]

## [Block Elements](https://support.typora.io/Markdown-Reference/#block-elements)

### Title

标题`#`在行首使用 1-6 个哈希 ( ) 字符，对应于标题级别 1-6。例如：

```
# This is an H1

## This is an H2

###### This is an H6
```



### Quote

Markdown 使用电子邮件样式 > 字符来进行块引用。它们呈现为：

```
> This is a blockquote with two paragraphs. This is first paragraph.
>
> This is second paragraph. Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> This is another blockquote with one paragraph. There is three empty line to separate two blockquotes.
```

### List

键入`* list item 1`将创建一个无序列表。（`*`符号可以替换为`+`或`-`。）

键入`1. list item 1`将创建一个有序列表。

例如：

```
## un-ordered list
*   Red
*   Green
*   Blue

## ordered list
1.  Red
2. 	Green
3.	Blue
```

### TaskList(Checkbox)

任务列表是带有标记为 [ ] 或 [x]（不完整或完整）的项目的列表。例如：

```
- [ ] a task list item
- [ ] list syntax required
- [ ] normal **formatting**, @mentions, #1234 refs
- [ ] incomplete
- [x] completed
```

### Code

Typora 仅支持 GitHub Flavored Markdown 中的栅栏，不支持原始代码块样式。

使用围栏很容易：输入 ``` 并按`return`。在 ``` 后面添加一个可选的语言标识符，Typora 通过语法高亮来运行它：

````
Here's an example:

```
function test() {
  console.log("notice the blank line before this function?");
}
```

syntax highlighting:
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
````

### Table

```
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```

还可以在表格中包含内联 Markdown，例如链接、粗体、斜体或删除线。

通过`:`在标题行中包含冒号 ( )，您可以将该列中的文本设置为左对齐、右对齐或居中对齐：

```
| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
```

### footnotes

一般把脚注放到文章末尾

```
You can create footnotes like this[^fn1] and this[^fn2].

[^fn1]: Here is the *text* of the first **footnote**.
[^fn2]: Here is the *text* of the second **footnote**.
```

### 横线

****

```
***

---
```



## Span Elements

### Link

This is [an example](http://example.com/ "Title") inline link. [This link](http://example.net/) has no title attribute.

#### Inline link

This is [an example](http://example.com/ "Title") inline link.

```
This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.
```



#### Internal link

只能跳转到标题

```
Hold down Cmd (on Windows: Ctrl) 
click on [this link](#block-elements) to jump to header `Block Elements`. 
```

like [this](#Internal link)

#### Reference Links

This is [an example][id] reference-style link.

一般把 id 放到文章末尾

```
This is [an example][id] reference-style link.

Then, anywhere in the document, you define your link label on a line by itself like this:

[id]: http://example.com/  "Optional Title Here"
```

[id]: http://example.com/	"Optional Title Here"

### Picture

图片在

```
![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")
```



