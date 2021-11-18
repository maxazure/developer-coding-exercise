import { useRequest, Link } from 'umi';
import { queryPost } from '@/services/post';
import Loading from '@/components/Loading';

const Posts = (props: { match: { params: { url: string; }; }; }) => {
  const {data,error, loading} = useRequest(() => queryPost(props.match.params.url));
  const createMarkup = (text: string) => ({ __html: text });

  if (error) {
    return <div>failed to load</div>
  }

  if (loading) {
    return <Loading message='Loading a post...' />
  }

  const post = data.post
  return (
    <div className='main'>
      <div className='bg'></div>
      <div className='bd'>
        <h1 className='title'>{post.title} </h1>
        <div className='content' dangerouslySetInnerHTML={createMarkup(post.content)}></div>
        <p><b>Author:</b> {post.author}</p>
        <p><b>TAGS:</b> {post.tags.map((x:string)=>x.replace(/^\S/, s => s.toUpperCase())).join(', ')}</p>
        <p><Link to="/">BACK</Link></p>
      </div>
    </div>
  );
};

export default Posts;