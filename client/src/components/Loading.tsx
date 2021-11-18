const Loading: React.FC<{ message: string }> = ({message}) => {
        return <div style={{ backgroundColor: "rgba(255,255,255,0.8)", width: "860px", height: "100%", position: "fixed", display: "table", textAlign: "center" }}>
        <div style={{ verticalAlign: "middle", display: "table-cell" }}>{message}</div>
    </div>;
}
export default Loading;