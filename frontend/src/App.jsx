import UploadPDF from "./components/UploadPDF";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">

      <div className="max-w-4xl mx-auto p-8">

        <h1 className="text-4xl font-bold text-center mb-8">

          PDF RAG Chatbot 🤖

        </h1>

        <UploadPDF/>

        <ChatBox/>
        
      </div>
    </div>

  )

}


export default App