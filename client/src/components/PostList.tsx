import { List, Typography } from 'antd';
const { Link } = Typography;

const PostList: React.FC<{
  posts: { id: number; title: string; url: string }[];
}> = ({ posts }) => {
  return (
    <List
      header={<h1>Mediasuite Blog Demo</h1>}
      dataSource={posts}
      rowKey="id"
      size="large"
      renderItem={(item) => (
        <List.Item>
          <Link href={'posts/' + item.url}>{item.title}</Link>
        </List.Item>
      )}
    />
  );
};

export default PostList;
