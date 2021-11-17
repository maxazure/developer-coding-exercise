import { useRequest } from 'umi';
import { queryPostList } from '@/services/post';
import PostList from '@/components/PostList';

export default function IndexPage() {

  const res = useRequest(() => queryPostList()); 

  if (res.loading) {
    return <div>loading...</div>
  }

  const postList = res.data
  return (
    <div className='main'>
      <div className='bg'></div>
      <div className='bd'>
        <h1 className='site-title'>Mediasuite Blog Demo</h1>
        <PostList posts={postList} />
      </div>
      
      
    </div>

  );
}
