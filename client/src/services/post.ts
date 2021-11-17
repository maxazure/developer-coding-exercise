import { request } from 'umi';

/** Get posts GET /api/posts */
export async function queryPostList() {
  return request<API.PostListItem>('/api/posts/', {
    method: 'GET',
  });
}

/** Get posts GET /api/post/xxx-xxx */
export async function queryPost(url: string) {
  if (url === undefined) {
    return null;
  }
  return request<API.Post>('/api/posts/' + url + '/');
}