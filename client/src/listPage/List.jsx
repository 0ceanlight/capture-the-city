export const ListView = () => {
    let maxPreviewLen = 64;

    let uploads = [
        {link: "https://www.google.com", title: "title1", content: "the brown fox jumped over the lazy dog which went down the tum slide at hackaTUM"},
        {link: "https://archlinux.org/", title: "title2", content: "never gonna give you up never gonna let you down never gonna run around or desert you. I just wanna tell you how I'm feeling!"}
    ]

    return (
        <div className="list_cards">
            { /* loop through uploads array */ }
            {uploads.map((upload, i, length) => (
                <>
                <h3 className="upload_title" onClick={()=> window.open(upload.link)}>{upload.title}</h3>
                <p className="upload_content_preview">{upload.content.slice(0, maxPreviewLen) + "..."}</p>
                {/* line divider */}
                {(() => {
                    if (i + 1 < length) {
                        // TODO: omit line break at end
                    }
                })()}
                <hr></hr>
                </>
            ))}
        </div>
    )
}

export default ListView;