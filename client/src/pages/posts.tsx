import { useRequest } from 'umi';
import { queryPost } from '@/services/post';

const Posts = (props: { match: { params: { url: string; }; }; })  => {
  const res = useRequest(() => queryPost(props.match.params.url)); 
  const createMarkup = (text: string) => ({ __html: text }); 

  if (res.loading) {
    return <div>loading...</div>
  }
  
  const post = res.data
  return (
    <div className='main'>
      <div className='bg'></div>
      <div className='bd'>
        <h1 className='title'>{post.title} </h1>
        <div className='content' dangerouslySetInnerHTML={createMarkup(post.html_content)}></div>
        <p><b>Author:</b> {post.author}</p>
        <p><b>TAGS:</b> {post.tags}</p>
        <p><a href="/">BACK</a></p>
      </div>

    </div>
  );
};

export default Posts;