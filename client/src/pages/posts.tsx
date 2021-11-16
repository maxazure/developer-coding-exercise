import { useRequest } from 'umi';
import { queryPost } from '@/services/post';
import styles from './style.css';

const Posts = (props: { match: { params: { url: string; }; }; })  => {
  const res = useRequest(() => queryPost(props.match.params.url)); 
  const createMarkup = (text: string) => ({ __html: text }); 

  if (res.loading) {
    return <div>loading...</div>
  }
  
  const post = res.data
  return (
    <div className={styles.bd}>
      <h1>{post.title} </h1>
      
      <div dangerouslySetInnerHTML={createMarkup(post.html_content)}>
      </div>
      <p><b>Author:</b> {post.author}</p>
      <p><b>TAGS:</b> {post.tags}</p>
    </div>
  );
};

export default Posts;