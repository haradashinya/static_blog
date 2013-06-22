title: JavaでJSON
date: 2013-03-01

<pre>
"[{'content':'foo','href':'fff'},{'content':'bar','href':'ffff'}]"
</pre>


みたいなString jsonがあったら、

<pre>
public class Content {
	public String content;
	public String href;
	// ignore getter and setter.
}
</pre>

みたいにして、

	Type type = new TypeToken< Collection  <Content > >() {}.getType();

	List<Content>contents = gson.fromJson(json.toString(),type);


	for(Content content : contents){
		//content.href
		//content.content
	}


みたいにすればjsonデータを取得できる。



