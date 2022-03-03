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



