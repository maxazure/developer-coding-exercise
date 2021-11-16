import { useRequest } from 'umi';
import { queryPostList } from '@/services/post';
import PostList from '@/components/PostList';
import styles from './style.css';

export default function IndexPage() {

  const res = useRequest(() => queryPostList()); 

  if (res.loading) {
    return <div>loading...</div>
  }

  const postList = res.data
  return (
    <div className={styles.bd}>
      <PostList posts={postList} />
    </div>
  );
}
