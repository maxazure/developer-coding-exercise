const Loading: React.FC<{ message: string }> = ({message}) => {
    
        return <div className='loading'>
        <div className='msg'>{message}</div></div>;
}
export default Loading;