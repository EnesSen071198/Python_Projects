# dotenv modülünden load_dotenv fonksiyonunu içe aktarır.
# Bu, çevresel değişkenleri bir ".env" dosyasından yüklememizi sağlar.
from dotenv import load_dotenv

# langchain_core modülünden belirli sınıflar ve işlevler içe aktarılır.
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# langchain_openai modülünden ChatOpenAI sınıfı içe aktarılır.
# Bu sınıf OpenAI ile etkileşim için kullanılır.
from langchain_openai import ChatOpenAI

# .env dosyasındaki çevresel değişkenleri yükler.
load_dotenv()

# ChatOpenAI modeli oluşturulur. Bu, OpenAI tabanlı bir sohbet modeli örneğidir.
model = ChatOpenAI()

# Mesaj geçmişlerini saklamak için bir sözlük oluşturulur.
store = {}

# Bir oturum kimliğine göre mesaj geçmişini döndüren bir fonksiyon tanımlanır.
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    # Eğer sözlükte oturum kimliği yoksa, yeni bir mesaj geçmişi eklenir.
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    # Oturum kimliğine ait mesaj geçmişi döndürülür.
    return store[session_id]

# Sohbet için bir istem şablonu (prompt) tanımlanır.
prompt = ChatPromptTemplate.from_messages(
    [
        # Sistem mesajı, yapay zekanın rolünü tanımlar.
        ("system", "You are a helpful assistant and answer all questions to the best of your ability"),
        # Mesaj geçmişini yerleştirmek için bir placeholder (yer tutucu) kullanılır.
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# İstem şablonu ve model, bir işlem zinciri oluşturmak için birleştirilir.
chain = prompt | model

# Yapılandırma için bir sözlük tanımlanır.
config = {"configurable": {"session_id": "abc123"}}

# Mesaj geçmişiyle birleştirilebilir bir çalıştırıcı (runnable) tanımlanır.
with_message_history = RunnableWithMessageHistory(chain, get_session_history)

# Ana blok, programın doğrudan çalıştırıldığında çalışmasını sağlar.
if __name__ == "__main__":
    # Sonsuz bir döngü oluşturulur, kullanıcıdan sürekli giriş alınır.
    while True:
        # Kullanıcı girdisi alınır.
        user_input = input("> ")
        # Kullanıcı mesajı ile mesaj geçmişi işlenir ve çıktı alınır.
        for r in with_message_history.stream(
            [
                # Kullanıcı mesajını temsil eden bir HumanMessage nesnesi oluşturulur.
                HumanMessage(content=user_input),
            ],
            config=config,  # Yapılandırma ile birlikte işlenir.
        ):
            # Her cevabı anında yazdırır (satır sonunda boşluk ekler).
            print(r.content, end="")
