import os
from src.synthia.validator.text_validator import TextValidator, InputGenerator, ValidatorSettings, AnthropicModule, OpenAIEmbedder, OpenAISettings
from communex.client import CommuneClient, Keypair
from communex._common import get_node_url
from dotenv import load_dotenv

load_dotenv()

client = CommuneClient(
    url = get_node_url() or "",
    num_connections=1,
    wait_for_finalization=True
)
settings = ValidatorSettings(
    api_key = os.getenv("ANTHROPIC_API_KEY") or "",
    temperature = 0.2,
    max_tokens = 1000,
    iteration_interval = 1200,
    hf_uploader_ss58="5EX6ixabe8fiWHySw4SYaJAkaHLKeqSJ3rv7so2FrLC2cfGV",
    model = "claude-3-opus-20240229"
)

llm = AnthropicModule()
    
inputgenerator = InputGenerator(llm)

openai_settings = OpenAISettings(
    api_key = os.getenv("OPENAI_API_KEY") or ""
)

key = Keypair(
    crypto_type=1,
    public_key=os.getenv("public_key"),
    private_key=os.getenv("private_key"),
    ss58_address=os.getenv("ss58_address"),
    seed_hex=os.getenv("seed_hex"),
    ss58_format=os.getenv("ss58_format")   
)

def launch():
    vali = TextValidator(
        key=key,
        netuid=3,
        client=client,
        embedder=OpenAIEmbedder(openai_settings=openai_settings)
    )
    vali.validation_loop()