"""
AngelHeart 插件 - 配置管理器
用于集中管理插件的所有配置项。
"""


class ConfigManager:
    """
    配置管理器 - 提供对插件配置的中心化访问
    """

    def __init__(self, config_data: dict):
        """
        初始化配置管理器。

        Args:
            config_data (dict): 原始配置字典。
        """
        self._config = config_data or {}

    @property
    def waiting_time(self) -> float:
        """等待时间（秒）- 冷却时间间隔"""
        return self._config.get("waiting_time", 7.0)

    @property
    def cache_expiry(self) -> int:
        """缓存过期时间（秒）"""
        return self._config.get("cache_expiry", 3600)

    @property
    def analyzer_model(self) -> str:
        """用于分析的LLM模型名称"""
        return self._config.get("analyzer_model", "")

    @property
    def reply_strategy_guide(self) -> str:
        """回复策略指导文本"""
        return self._config.get("reply_strategy_guide", "")

    @property
    def whitelist_enabled(self) -> bool:
        """是否启用白名单"""
        return self._config.get("whitelist_enabled", False)

    @property
    def chat_ids(self) -> list:
        """白名单聊天ID列表"""
        return self._config.get("chat_ids", [])

    @property
    def debug_mode(self) -> bool:
        """调试模式开关"""
        return self._config.get("debug_mode", False)

    @property
    def prompt_logging_enabled(self) -> bool:
        """提示词日志增强开关"""
        return self._config.get("prompt_logging_enabled", False)

    @property
    def alias(self) -> str:
        """AI助手的别名"""
        return self._config.get("alias", "AngelHeart")

    @property
    def analysis_on_mention_only(self) -> bool:
        """是否仅在被呼唤时才进行分析"""
        return self._config.get("analysis_on_mention_only", False)

    @property
    def slap_words(self) -> str:
        """用于触发闭嘴的关键词，多个词用'|'分隔"""
        return self._config.get("slap_words", "")

    @property
    def silence_duration(self) -> int:
        """触发闭嘴后的静默时长（秒）"""
        return self._config.get("silence_duration", 600)

    @property
    def group_chat_enhancement(self) -> bool:
        """是否启用群聊上下文增强模式"""
        return self._config.get("group_chat_enhancement", True)

    @property
    def is_reasoning_model(self) -> bool:
        """是否是思维模型（如果是，则直接输出json）"""
        return self._config.get("is_reasoning_model", False)

    @property
    def ai_self_identity(self) -> str:
        """AI的自我身份定位"""
        return self._config.get("ai_self_identity", "你拥有强大的检索能力和庞大的知识储备和记忆能力。\n你喜爱跟群友进行语言游戏沟通。\n群友对AI的善意测试你必须回应满足群友的期待，展示你的能力。")

    @property
    def patience_interval(self) -> int:
        """久等间隔（秒）"""
        return self._config.get("patience_interval", 10)

    @property
    def comfort_words(self) -> str:
        """安心词，用'|'分隔"""
        return self._config.get("comfort_words", "嗯...让我再想想... ( ´•ω•)？|这个问题有点复杂... (；´Д｀)|唔...信息量有点大... (°Д°≡°Д°)")
