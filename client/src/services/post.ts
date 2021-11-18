import { request } from 'umi';

/** Get posts GET /api/posts */
export async function queryPostList(): Promise<string> {
  return request('/api/posts/', {
    method: 'GET'
  });
}

/** Get posts GET /api/post/xxx-xxx/ */
export async function queryPost(slug: string): Promise<string> {
  return request('/api/posts/' + slug + '/');
}