import { useRequest } from 'umi';
import { queryPostList } from '@/services/post';
import PostList from '@/components/PostList';
import Loading from '@/components/Loading';

const IndexPage = () => {

  const { data,error, loading } = useRequest(() => queryPostList()); 
  
  if (error) {
    return <div>failed to load</div>
  }
  
  if (loading) {
    return <Loading message='Loading homepage ...' />
  }

  return (
    <div className='main'>
      <div className='bg'></div>
      <div className='bd'>
        <h1 className='site-title'>Mediasuite Blog Demo</h1>
        <PostList posts={data.posts} />
      </div>
    </div>

  );
}

export default IndexPage;